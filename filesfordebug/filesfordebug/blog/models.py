# blog/models.py
import os
from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver


def blog_image_upload_path(instance, filename):
    return (
        os.path.join('blog', 'images', instance.slug, filename)
        .replace('\\', '/')
    )


def blog_video_upload_path(instance, filename):
    return f'blog/videos/{instance.slug}/{filename}'


class BlogPost(models.Model):
    STATUS_CHOICES = [
        ('draft', _('Draft')),
        ('published', _('Published')),
    ]

    # Core content (English + Italian)
    title_en = models.CharField(max_length=200, verbose_name=_("Title (EN)"))
    title_it = models.CharField(
        max_length=200,
        verbose_name=_("Title (IT)"),
        blank=True
    )
    slug = models.SlugField(unique=True, max_length=200, blank=True)

    body_en = RichTextField(verbose_name=_("Content (EN)"))
    body_it = RichTextField(verbose_name=_("Content (IT)"), blank=True)

    # Media
    featured_image = CloudinaryField('image', blank=True, null=True)
    video = CloudinaryField(resource_type='video', blank=True, null=True)

    # Metadata
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-published_at', '-created_at']
        verbose_name = _("Blog Post")
        verbose_name_plural = _("Blog Posts")

    def __str__(self):
        return self.title_en

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_en)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/blog/{self.slug}/"


# --- Auto-set published_at when status becomes "published" ---
@receiver(
    pre_save,
    sender=BlogPost,
    dispatch_uid="blogpost_set_published_at_once"
)
def set_published_at_on_publish(sender, instance, **kwargs):
    """
    Ensure published_at is set the first time a post is saved as 'published'.
    Does nothing if published_at is already set.
    """
    try:
        if instance.status == "published" and not instance.published_at:
            instance.published_at = timezone.now()
    except Exception:
        # Be defensive; never break saves because of this.
        pass
