from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import BlogPost


class BlogPostAdminForm(forms.ModelForm):
    body_en = forms.CharField(widget=CKEditorWidget(), label="Content (EN)")
    body_it = forms.CharField(widget=CKEditorWidget(), label="Content (IT)", required=False)

    class Meta:
        model = BlogPost
        fields = '__all__'


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm

    list_display = ("title_en", "status", "author", "created_at")
    list_filter = ("status", "created_at", "author")
    search_fields = ("title_en", "title_it", "body_en", "body_it")
    prepopulated_fields = {"slug": ("title_en",)}

    fieldsets = (
        ("English Content", {
            "fields": ("title_en", "body_en")
        }),
        ("Italian Content", {
            "fields": ("title_it", "body_it")
        }),
        ("Media", {
            "fields": ("featured_image", "video")
        }),
        ("Metadata", {
            "fields": ("slug", "author", "status", "published_at")
        }),
    )
