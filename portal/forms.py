# portal/forms.py
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from ckeditor.widgets import CKEditorWidget

from blog.models import BlogPost
from flyers.models import Flyer

User = get_user_model()

# ---- Feature groups shown as checkboxes ----
FEATURE_GROUP_NAMES = ["BLOG", "SCHEDULE", "FLYERS"]


# ---- Create User (used by Leanne) ----
class PortalUserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    is_active = forms.BooleanField(
        required=False, initial=True, label="Active"
    )
    features = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[(name, name) for name in FEATURE_GROUP_NAMES],
        label="Feature access",
        help_text=(
            "Tick the sections this user can access from the portal dashboard."
        ),
    )

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "is_active")

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError(
                "A user with that username already exists."
            )
        return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        if email and User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                "A user with that email already exists."
            )
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.is_active = self.cleaned_data.get("is_active", True)
        # Give portal access
        user.is_staff = True
        if commit:
            user.save()
            selected = self.cleaned_data.get("features", [])
            groups = Group.objects.filter(name__in=selected)
            user.groups.set(groups)
        return user


# ---- Update User (owner-only edit; no password fields) ----
class PortalUserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=False)
    is_active = forms.BooleanField(required=False, label="Active")
    features = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[(name, name) for name in FEATURE_GROUP_NAMES],
        label="Feature access",
    )

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "is_active")
        widgets = {
            "username": forms.TextInput(attrs={"readonly": "readonly"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        current = list(self.instance.groups.values_list("name", flat=True))
        self.fields["features"].initial = [
            g for g in FEATURE_GROUP_NAMES if g in current
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            selected = self.cleaned_data.get("features", [])
            groups = Group.objects.filter(name__in=selected)
            user.groups.set(groups)
        return user


# ---- Blog form ----
class BlogPostForm(forms.ModelForm):
    body_en = forms.CharField(widget=CKEditorWidget())
    body_it = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = BlogPost
        fields = [
            "title_en", "title_it",
            "slug",
            "body_en", "body_it",
            "featured_image", "video",
            "status", "published_at",
        ]


# ---- Flyer form (robust to model differences) ----
class FlyerForm(forms.ModelForm):
    class Meta:
        model = Flyer
        fields = "__all__"  # don't hard-code; model may differ across envs
        # widgets will be set dynamically in __init__

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Attach CKEditor to description fields if present
        for fld in ("description_en", "description_it"):
            if fld in self.fields:
                self.fields[fld].widget = CKEditorWidget()

        # HTML5 date picker if event_date exists
        if "event_date" in self.fields:
            self.fields["event_date"].widget = forms.DateInput(
                attrs={"type": "date"}
            )

        # Hide sort_order (managed via drag-and-drop UI)
        if "sort_order" in self.fields:
            self.fields["sort_order"].widget = forms.HiddenInput()
