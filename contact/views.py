# contact/views.py
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from .forms import ContactForm
import requests
import logging

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

            # Use settings; don't hard-code Gmail here
            from_addr = settings.DEFAULT_FROM_EMAIL
            to_addr = getattr(
                settings,
                "CONTACT_TO_EMAIL",
                settings.DEFAULT_FROM_EMAIL,
            )

            # Try to send the email; if it fails, stay on page and show error
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
                    request,
                    "We couldn't deliver your message right now. "
                    f"Please try again shortly or email us directly at "
                    f"{to_addr}."
                )
                return render(
                    request,
                    "contact.html",
                    {
                        "form": form,
                        "show_modal": False,
                        "GOOGLE_MAPS_API_KEY": settings.GOOGLE_MAPS_API_KEY,
                    },
                    status=500,
                )

            # Optional: subscribe to Mailchimp (non-blocking)
            if data.get("subscribe"):
                api_key = getattr(settings, "MAILCHIMP_API_KEY", None)
                list_id = getattr(settings, "MAILCHIMP_AUDIENCE_ID", None)
                if api_key and list_id:
                    try:
                        dc = api_key.split("-")[-1]
                        url = (
                            f"https://{dc}.api.mailchimp.com/3.0/lists/"
                            f"{list_id}/members"
                        )
                        payload = {
                            "email_address": data["email"],
                            "status": "subscribed",
                            "merge_fields": {"FNAME": data["full_name"]},
                        }
                        headers = {"Authorization": f"apikey {api_key}"}
                        r = requests.post(
                            url,
                            json=payload,
                            headers=headers,
                            timeout=10,
                        )
                        r.raise_for_status()
                    except Exception:
                        # Log but don't block the flow
                        logger.warning(
                            "Mailchimp subscribe failed", exc_info=True
                        )

            return redirect(
                f"{request.path}?sent=1"
            )  # 302 on success
            return redirect(f"{request.path}?sent=1")  # 302 on success

        # INVALID → show why and return 400
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
