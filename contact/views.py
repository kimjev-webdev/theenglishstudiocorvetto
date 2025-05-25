from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
import requests
import os


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

        # Send the email
        send_mail(
            subject=f"New Contact Form Submission: {data['subject']}",
            message=message,
            from_email="theenglishstudio.corvetto@gmail.com",
            recipient_list=["theenglishstudio.corvetto@gmail.com"],
            reply_to=[data['email']],
        )

        # If subscribed, add to Mailchimp
        if data.get("subscribe"):
            mailchimp_api_key = os.getenv("MAILCHIMP_API_KEY")
            mailchimp_list_id = os.getenv("MAILCHIMP_AUDIENCE_ID")
            datacenter = mailchimp_api_key.split('-')[-1]

            url = (
                f"https://{datacenter}.api.mailchimp.com/3.0/"
                f"lists/{mailchimp_list_id}/members"
            )

            payload = {
                "email_address": data["email"],
                "status": "subscribed",
                "merge_fields": {
                    "FNAME": data["full_name"]
                }
            }

            headers = {
                "Authorization": f"apikey {mailchimp_api_key}"
            }

            try:
                response = requests.post(url, json=payload, headers=headers)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(f"Mailchimp error: {e}")

# After successful form submission:
        return render(
            request,
            "contact.html",
            {"form": ContactForm(), "show_modal": True}
        )

    # On initial load or error:
    return render(request, "contact.html", {"form": form})
