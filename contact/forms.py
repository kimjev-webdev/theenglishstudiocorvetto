# contact/forms.py
from django import forms
from django.utils.translation import gettext_lazy as _

SUBJECT_CHOICES = [
    ("After School Club", "After School Club"),
    ("Private Lessons", "Private Lessons"),
    ("Business English Lessons", "Business English Lessons"),
    ("General English Lessons", "General English Lessons"),
    ("IELTS Enquiry", "IELTS Enquiry"),
    ("Events", "Events"),
    ("Other", "Other"),
]

# Text that appears as the placeholder option in your <select>
# Include both raw English and a translatable version so it works in /en
# and /it.
PLACEHOLDER_LABELS = {"Select an option", _("Select an option")}


class ContactForm(forms.Form):
    full_name = forms.CharField(
        max_length=255,
        label=_("Full Name"),
    )
    email = forms.EmailField(
        label=_("Email"),
    )
    # Your template marks phone as required*.
    # Keep server-side lenient to avoid false negatives.
    phone = forms.CharField(
        max_length=30,
        required=False,
        label=_("Phone"),
    )
    # Use CharField so translated option text or custom text doesn't fail
    # ChoiceField validation.
    subject = forms.CharField(
        max_length=120,
        label=_("Subject"),
    )
    message = forms.CharField(
        widget=forms.Textarea,
        label=_("Message"),
    )
    subscribe = forms.BooleanField(
        required=False,
        label=_("Subscribe to newsletter"),
    )

    def clean_subject(self) -> str:
        """Accept the posted subject text (works with translated UI),
        but reject the placeholder and normalize to a canonical value
        when possible."""
        s = (self.cleaned_data.get("subject") or "").strip()
        if not s or s in PLACEHOLDER_LABELS:
            raise forms.ValidationError(_("Please select a subject."))
        # Try to normalize to one of our canonical subjects (case-insensitive).
        for value, label in SUBJECT_CHOICES:
            if s.lower() == value.lower() or s.lower() == label.lower():
                return value  # store canonical value
        return s  # fallback: keep what the user sent

    def clean_full_name(self):
        name = (self.cleaned_data.get("full_name") or "").strip()
        if not name:
            raise forms.ValidationError(_("This field is required."))
        return name

    def clean_message(self):
        msg = (self.cleaned_data.get("message") or "").strip()
        if not msg:
            raise forms.ValidationError(_("This field is required."))
        return msg
