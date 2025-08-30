# contact/views.py
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from .forms import ContactForm
import requests
import logging
import hashlib

logger = logging.getLogger(__name__)


def contact_view(request):
    form = ContactForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data

            # Build plain-text body
            body = (
                f"Name: {data['full_name']}\n"
                f"Email: {data['email']}\n"
                f"Phone: {data.get('phone', 'N/A')}\n"
                f"Subject: {data['subject']}\n"
                f"Subscribed: {'Yes' if data.get('subscribe') else 'No'}\n\n"
                f"Message:\n{data['message']}"
            )

            # Sender/recipient from settings (avoid DMARC issues)
            from_addr = settings.DEFAULT_FROM_EMAIL
            to_addr = getattr(
                settings, "CONTACT_TO_EMAIL", settings.DEFAULT_FROM_EMAIL
            )

            # Send email (fail loud; do not redirect on failure)
            try:
                msg = EmailMessage(
                    subject=f"New Contact: {data['subject'].strip()}",
                    body=body,
                    from_email=from_addr,
                    to=[to_addr],
                    reply_to=[data["email"]],
                )
                sent = msg.send(fail_silently=False)
                if sent != 1:
                    raise RuntimeError(f"EmailMessage.send returned {sent}")
            except Exception:
                logger.exception("Contact email failed to send")
                messages.error(
                    f"Please try again shortly or email us directly at "
                    f"{to_addr}."
                    "We couldn't deliver your message right now. "
                    (
                        f"Please try again shortly or email us directly at "
                        f"{to_addr}."
                    )
                )
            return render(
                request,
                "contact.html",
                {
                    "form": form,
                    "show_modal": False,
                    "GOOGLE_MAPS_API_KEY": settings.GOOGLE_MAPS_API_KEY,
                },
            )
            # Optional: subscribe to Mailchimp (non-blocking,
            # idempotent upsert)

            # Optional: subscribe to Mailchimp (non-blocking,
            # idempotent upsert)
            if data.get("subscribe"):
                api_key = getattr(settings, "MAILCHIMP_API_KEY", "") or ""
                list_id = getattr(settings, "MAILCHIMP_AUDIENCE_ID", "") or ""
                if api_key and list_id:
                    try:
                        dc = api_key.split("-")[-1]  # e.g. 'us9'
                        email_lower = data["email"].strip().lower()
                        sub_hash = hashlib.md5(
                            email_lower.encode()
                        ).hexdigest()
                        base = (
                            f"https://{dc}.api.mailchimp.com/3.0/lists/"
                            f"{list_id}"
                        )
                        url = f"{base}/members/{sub_hash}"
                        payload = {
                            "email_address": email_lower,
                            "status_if_new": "pending",
                            "merge_fields": {"FNAME": data["full_name"]},
                        }
                        headers = {"Authorization": f"apikey {api_key}"}
                        r = requests.put(
                            url,
                            json=payload,
                            headers=headers,
                            timeout=10,
                        )
                        r.raise_for_status()

                        # Optional: tag the contact (ignore failures)
                        try:
                            tags_url = f"{base}/members/{sub_hash}/tags"
                            requests.post(
                                tags_url,
                                json={
                                    "tags": [
                                        {
                                            "name": "Website",
                                            "status": "active"
                                        }
                                    ]
                                },
                                headers=headers,
                                timeout=10,
                            )
                        except Exception:
                            logger.info(
                                "Mailchimp tag add failed", exc_info=True
                            )

                    except requests.HTTPError as e:
                        # Log exact Mailchimp error
                        try:
                            err_text = e.response.text
                        except Exception:
                            err_text = "<no response body>"
                        logger.warning(
                            "Mailchimp upsert failed %s: %s",
                            getattr(e.response, "status_code", "?"),
                            err_text,
                        )
                    except Exception:
                        logger.warning(
                            "Mailchimp subscribe failed", exc_info=True
                        )
                else:
                    logger.info("Mailchimp skipped: keys not configured")

            # Success
            return redirect(f"{request.path}?sent=1")  # 302 on success

        # INVALID → show why
        logger.info("Contact form invalid: %s", dict(form.errors))
        messages.error(request, "Please fix the errors below.")

    show_modal = request.GET.get("sent") == "1"
    return render(
        request,
        "contact.html",
        {
            "form": form,
            "show_modal": show_modal,
            "GOOGLE_MAPS_API_KEY": settings.GOOGLE_MAPS_API_KEY,
        },
    )
