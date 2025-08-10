from django.shortcuts import render, get_object_or_404
from .models import BlogPost


def blog_list(request):
    # Show published posts, newest first
    # (fallback to id if published_at is null)
    posts = (BlogPost.objects
             .filter(status='published')
             .order_by('-published_at', '-id'))
    return render(request, 'blog/blog_list.html', {'posts': posts})


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, status='published')

    # Guard against NULL published_at (which caused your 500)
    if post.published_at:
        # "Next" = newer post, "Previous" = older post
        next_post = (
            BlogPost.objects
            .filter(
                status='published',
                published_at__gt=post.published_at
            )
            .order_by('published_at')
            .first()
        )
        previous_post = (
            BlogPost.objects
            .filter(
                status='published',
                published_at__lt=post.published_at
            )
            .order_by('-published_at')
            .first()
        )
    else:
        # Fallback if this post has no published_at yet
        next_post = (BlogPost.objects
                     .filter(status='published', id__gt=post.id)
                     .order_by('id')
                     .first())
        previous_post = (BlogPost.objects
                         .filter(status='published', id__lt=post.id)
                         .order_by('-id')
                         .first())

    return render(request, 'blog/blog_detail.html', {
        'post': post,
        'previous_post': previous_post,  # older
        'next_post': next_post,          # newer
    })
