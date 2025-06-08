from django.shortcuts import render, get_object_or_404
from .models import BlogPost


def blog_list(request):
    posts = BlogPost.objects.filter(status='published')
    return render(request, 'blog/blog_list.html', {'posts': posts})


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, status='published')

    # Get previous and next based on publication date
    previous_post = BlogPost.objects.filter(
        published_at__gt=post.published_at,
        status='published'
    ).order_by('published_at').first()

    next_post = BlogPost.objects.filter(
        published_at__lt=post.published_at,
        status='published'
    ).order_by('-published_at').first()

    return render(request, 'blog/blog_detail.html', {
        'post': post,
        'previous_post': next_post,
        'next_post': previous_post,
    })
