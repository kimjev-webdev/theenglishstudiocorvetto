from django import forms

SUBJECT_CHOICES = [
    ("After School Club", "After School Club"),
    ("Private Lessons", "Private Lessons"),
    ("Business English Lessons", "Business English Lessons"),
    ("General English Lessons", "General English Lessons"),
    ("IELTS Enquiry", "IELTS Enquiry"),
    ("Events", "Events"),
    ("Other", "Other"),
]


class ContactForm(forms.Form):
    full_name = forms.CharField(
        max_length=255,
        label="Full Name"
    )
    email = forms.EmailField(
        label="Email"
    )
    phone = forms.CharField(
        max_length=30,
        required=False,
        label="Phone"
    )
    subject = forms.ChoiceField(
        choices=[('', 'Select an option')] + SUBJECT_CHOICES,
        label="Subject"
    )
    message = forms.CharField(
        widget=forms.Textarea,
        label="Message"
    )
    subscribe = forms.BooleanField(
        required=False,
        label="Subscribe to newsletter"
    )
