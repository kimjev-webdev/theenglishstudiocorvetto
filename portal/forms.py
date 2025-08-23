# portal/forms.py
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from ckeditor.widgets import CKEditorWidget

from blog.models import BlogPost
from flyers.models import Flyer

# ----------------------------
# FEATURE GROUPS (checkboxes)
# ----------------------------
FEATURE_GROUP_NAMES = ["BLOG", "SCHEDULE", "FLYERS"]

# ----------------------------
# CREATE USER FORM (portal)
# ----------------------------
User = get_user_model()


class PortalUserCreateForm(UserCreationForm):
    email = forms.EmailField(
        required=True
    )
    is_active = forms.BooleanField(
        required=False,
        initial=True,
        label="Active"
    )
    features = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[(name, name) for name in FEATURE_GROUP_NAMES],
        label="Feature access",
        help_text=(
            "Tick the sections this user can access from the portal "
            "dashboard."
        ),
    )

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "is_active")

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(
            username__iexact=username
        ).exists():
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
        # Keep portal users as staff (so they can sign in to the portal area).
        # Remove or set False if you plan to gate purely by groups instead.
        user.is_staff = True

        if commit:
            user.save()
            selected = self.cleaned_data.get("features", [])
            groups = Group.objects.filter(name__in=selected)
            # replace any existing groups with exactly these
            user.groups.set(groups)
        return user


# ----------------------------
# BLOG FORM
# ----------------------------
class BlogPostForm(forms.ModelForm):
    body_en = forms.CharField(widget=CKEditorWidget())
    body_it = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = BlogPost
        fields = [
            'title_en', 'title_it',
            'slug',
            'body_en', 'body_it',
            'featured_image', 'video',
            'status', 'published_at'
        ]


# ----------------------------
# FLYER FORM
# ----------------------------
class FlyerForm(forms.ModelForm):
    description_en = forms.CharField(widget=CKEditorWidget())
    description_it = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Flyer
        fields = [
            'title_en', 'title_it',
            'description_en', 'description_it',
            'extra_info_en', 'extra_info_it',
            'image', 'event_date'
        ]
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date'})
        }
