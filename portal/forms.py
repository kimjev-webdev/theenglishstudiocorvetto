from django import forms
from ckeditor.widgets import CKEditorWidget  # ✅ import CKEditorWidget
from blog.models import BlogPost

class BlogPostForm(forms.ModelForm):
    # ✅ Use CKEditor for both language body fields
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
