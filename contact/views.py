# contact/views.py
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from .forms import ContactForm
import requests


def contact_view(request):
    form = ContactForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data

            body = (
                f"Name: {data['full_name']}\n"
                f"Email: {data['email']}\n"
                f"Phone: {data.get('phone', 'N/A')}\n"
                f"Subject: {data['subject']}\n"
                f"Subscribed: {'Yes' if data.get('subscribe') else 'No'}\n\n"
                f"Message:\n{data['message']}"
            )
            try:
                EmailMessage(
                    subject=f"New Contact: {data['subject']}",
                    body=body,
                    from_email="theenglishstudio.corvetto@gmail.com",
                    to=["theenglishstudio.corvetto@gmail.com"],
                    reply_to=[data["email"]],
                ).send(fail_silently=False)
            except Exception as e:
                # don’t block UX; log it
                print("Email send error:", e)

            if data.get("subscribe"):
                try:
                    api_key = settings.MAILCHIMP_API_KEY
                    list_id = settings.MAILCHIMP_AUDIENCE_ID
                    dc = api_key.split("-")[-1]
                    url = (
                        f"https://{dc}.api.mailchimp.com/3.0/lists/"
                        f"{list_id}/members"
                    )
                    payload = {
                        "email_address": data["email"],
                        "status": "subscribed",
                        "merge_fields": {
                            "FNAME": data["full_name"]
                        },
                    }
                    headers = {"Authorization": f"apikey {api_key}"}
                    requests.post(
                        url,
                        json=payload,
                        headers=headers,
                        timeout=10
                    ).raise_for_status()
                except Exception as e:
                    print("Mailchimp error:", e)

            messages.success(request, "Thanks! We’ll be in touch soon.")
            return redirect(f"{request.path}?sent=1")  # <-- must be 302

        # INVALID → show why
        print("Contact form INVALID:", form.errors)
        messages.error(request, "Please fix the errors below.")

    show_modal = request.GET.get("sent") == "1"
    return render(
        request,
        "contact.html",
        {
            "form": form,
            "show_modal": show_modal,
            "GOOGLE_MAPS_API_KEY": (
                settings.GOOGLE_MAPS_API_KEY  # leave your template var as-is
            ),
        },
    )
