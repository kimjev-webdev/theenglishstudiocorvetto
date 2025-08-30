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
                f"Subscribed: "
                f"{'Yes' if data.get('subscribe') else 'No'}\n\n"
                f"Message:\n{data['message']}"
            )

            # Sender/recipient from settings (avoid DMARC issues)
            from_addr = settings.DEFAULT_FROM_EMAIL
            to_addr = getattr(
                settings,
                "CONTACT_TO_EMAIL",
                settings.DEFAULT_FROM_EMAIL,
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
                    raise RuntimeError(
                        f"EmailMessage.send returned {sent}"
                    )
            except Exception:
                logger.exception("Contact email failed to send")
                messages.error(
                    request,
                    (
                        "We couldn't deliver your message right now. "
                        "Please try again shortly or email us directly at "
                        f"{to_addr}."
                    ),
                )
                return render(
                    request,
                    "contact.html",
                    {
                        "form": form,
                        "show_modal": False,
                        "GOOGLE_MAPS_API_KEY": (
                            settings.GOOGLE_MAPS_API_KEY
                        ),
                    },
                    status=500,
                )

            # Optional: subscribe to Mailchimp (non-blocking)
            if data.get("subscribe"):
                api_key = getattr(
                    settings, "MAILCHIMP_API_KEY", ""
                ) or ""
                list_id = getattr(
                    settings, "MAILCHIMP_AUDIENCE_ID", ""
                ) or ""

                if api_key and list_id:
                    try:
                        dc = api_key.split("-")[-1]        # e.g. 'us9'
                        email_lower = (
                            data["email"].strip().lower()
                        )
                        sub_hash = hashlib.md5(
                            email_lower.encode()
                        ).hexdigest()

                        base = (
                            f"https://{dc}.api.mailchimp.com/3.0/"
                            f"lists/{list_id}"
                        )
                        headers = {
                            "Authorization": f"apikey {api_key}"
                        }
                        member_url = f"{base}/members/{sub_hash}"

                        # Check current status
                        r = requests.get(
                            member_url,
                            headers=headers,
                            timeout=10,
                        )
                        if r.status_code == 404:
                            # New → create as *subscribed* (instant)
                            up = {
                                "email_address": email_lower,
                                "status": "subscribed",
                                "merge_fields": {
                                    "FNAME": data["full_name"]
                                },
                            }
                            requests.put(
                                member_url,
                                json=up,
                                headers=headers,
                                timeout=10,
                            ).raise_for_status()
                        else:
                            r.raise_for_status()
                            status = (
                                r.json().get("status") or ""
                            ).lower()

                            if status != "subscribed":
                                # Try to force subscribe; on compliance
                                # failure fall back to "pending".
                                try:
                                    requests.put(
                                        member_url,
                                        json={
                                            "status": "subscribed",
                                            "merge_fields": {
                                                "FNAME": data[
                                                    "full_name"
                                                ]
                                            },
                                        },
                                        headers=headers,
                                        timeout=10,
                                    ).raise_for_status()
                                except requests.HTTPError as e:
                                    logger.warning(
                                        "Mailchimp resubscribe blocked "
                                        "(%s): %s — falling back to "
                                        "'pending'",
                                        getattr(
                                            e.response, "status_code", "?"
                                        ),
                                        getattr(
                                            e.response, "text", ""
                                        ),
                                    )
                                    requests.put(
                                        member_url,
                                        json={
                                            "status": "pending",
                                            "merge_fields": {
                                                "FNAME": data[
                                                    "full_name"
                                                ]
                                            },
                                        },
                                        headers=headers,
                                        timeout=10,
                                    ).raise_for_status()
                            else:
                                # Already subscribed → refresh fields
                                try:
                                    requests.patch(
                                        member_url,
                                        json={
                                            "merge_fields": {
                                                "FNAME": data[
                                                    "full_name"
                                                ]
                                            }
                                        },
                                        headers=headers,
                                        timeout=10,
                                    )
                                except Exception:
                                    logger.info(
                                        "Mailchimp merge-field refresh "
                                        "failed",
                                        exc_info=True,
                                    )

                        # Optional: tag (best-effort)
                        try:
                            requests.post(
                                f"{base}/members/{sub_hash}/tags",
                                json={
                                    "tags": [
                                        {
                                            "name": "Website",
                                            "status": "active",
                                        }
                                    ]
                                },
                                headers=headers,
                                timeout=10,
                            )
                        except Exception:
                            logger.info(
                                "Mailchimp tag add failed",
                                exc_info=True,
                            )

                    except requests.HTTPError as e:
                        logger.warning(
                            "Mailchimp upsert failed %s: %s",
                            getattr(e.response, "status_code", "?"),
                            getattr(e.response, "text", ""),
                        )
                    except Exception:
                        logger.warning(
                            "Mailchimp subscribe failed",
                            exc_info=True,
                        )
                else:
                    logger.info(
                        "Mailchimp skipped: keys not configured"
                    )

            # Success → trigger thank-you modal via ?sent=1
            return redirect(f"{request.path}?sent=1")

        # INVALID → show why
        logger.info(
            "Contact form invalid: %s",
            dict(form.errors),
        )
        messages.error(
            request,
            "Please fix the errors below.",
        )

    # Show modal if redirected with ?sent=1
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
