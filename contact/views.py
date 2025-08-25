# contact/views.py
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from .forms import ContactForm
import requests


def contact_view(request):
    form = ContactForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data

        # Build email body
        body = (
            f"Name: {data['full_name']}\n"
            f"Email: {data['email']}\n"
            f"Phone: {data.get('phone', 'N/A')}\n"
            f"Subject: {data['subject']}\n"
            f"Subscribed to newsletter: "
            f"{'Yes' if data.get('subscribe') else 'No'}\n\n"
            f"Message:\n{data['message']}"
        )

        # Send email (with reply-to)
        try:
            EmailMessage(
                subject=f"New Contact Form Submission: {data['subject']}",
                body=body,
                from_email="theenglishstudio.corvetto@gmail.com",
                to=["theenglishstudio.corvetto@gmail.com"],
                reply_to=[data["email"]],
            ).send(fail_silently=False)
        except Exception as e:
            # Don’t fail the UX—log and proceed
            print(f"Email send error: {e}")

        # Optional: Mailchimp subscribe
        if data.get("subscribe"):
            try:
                api_key = settings.MAILCHIMP_API_KEY
                list_id = settings.MAILCHIMP_AUDIENCE_ID
                dc = api_key.split("-")[-1]  # datacenter suffix

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
                    url, json=payload, headers=headers, timeout=10
                )
                r.raise_for_status()
            except Exception as e:
                print(f"Mailchimp error: {e}")

        messages.success(request, "Thanks! We’ll be in touch soon.")
        # PRG: redirect so refresh doesn’t resubmit; modal will show on GET
        return redirect(f"{request.path}?sent=1")

    # GET or invalid POST → render page
    show_modal = request.GET.get("sent") == "1"

    return render(
        request,
        "contact.html",
        {
            "form": form,
            "show_modal": show_modal,  # your JS reads this to auto-open modal
            # leaving your maps key exactly as you had it:
            "google_maps_api_key": settings.GOOGLE_MAPS_API_KEY,
        },
    )
