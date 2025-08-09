from django.shortcuts import render
from django.conf import settings
from .forms import ContactForm
from django.core.mail import EmailMessage
import requests


def contact_view(request):
    form = ContactForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data

        # Format the message
        message = (
            f"Name: {data['full_name']}\n"
            f"Email: {data['email']}\n"
            f"Phone: {data.get('phone', 'N/A')}\n"
            f"Subject: {data['subject']}\n"
            f"Subscribed to newsletter: "
            f"{'Yes' if data.get('subscribe') else 'No'}\n\n"
            f"Message:\n{data['message']}"
        )

        # ✅ Send email with reply-to
        email = EmailMessage(
            subject=f"New Contact Form Submission: {data['subject']}",
            body=message,
            from_email="theenglishstudio.corvetto@gmail.com",
            to=["theenglishstudio.corvetto@gmail.com"],
            reply_to=[data["email"]],
        )
        email.send()

        # ✅ Subscribe to Mailchimp if opted-in
        if data.get("subscribe"):
            mailchimp_api_key = settings.MAILCHIMP_API_KEY
            mailchimp_list_id = settings.MAILCHIMP_AUDIENCE_ID
            datacenter = mailchimp_api_key.split('-')[-1]

            url = (
                f"https://{datacenter}.api.mailchimp.com/3.0/lists/"
                f"{mailchimp_list_id}/members"
            )
            payload = {
                "email_address": data["email"],
                "status": "subscribed",
                "merge_fields": {"FNAME": data["full_name"]}
            }
            headers = {
                "Authorization": f"apikey {mailchimp_api_key}"
            }

            try:
                response = requests.post(url, json=payload, headers=headers)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(f"Mailchimp error: {e}")

        print("✔️ Contact form submitted successfully — modal should show")

        return render(
            request,
            "contact.html",
            {
                "form": ContactForm(),
                "show_modal": True,
                "google_maps_api_key": settings.GOOGLE_MAPS_API_KEY,
                # Pass the API key to the template
            }
        )

    # ❌ GET or invalid form, render the form again
    return render(
        request,
        "contact.html",
        {
            "form": form,
            "google_maps_api_key": (
                settings.GOOGLE_MAPS_API_KEY
                # Pass the API key to the template
            ),
        }
    )
