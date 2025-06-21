from django import forms
from blog.models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            'title_en', 'title_it',
            'slug',
            'body_en', 'body_it',
            'featured_image', 'video',
            'status', 'published_at'
        ]
