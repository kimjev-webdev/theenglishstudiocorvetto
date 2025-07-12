from django import forms
from ckeditor.widgets import CKEditorWidget
from blog.models import BlogPost
from main.models import Flyer


# --- BLOG FORM ---
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


# --- FLYER FORM ---
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
