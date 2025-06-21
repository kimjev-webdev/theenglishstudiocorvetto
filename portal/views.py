from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from blog.models import BlogPost
from .forms import BlogPostForm


# 🔐 Function-based staff access check for dashboard
def staff_check(user):
    return user.is_authenticated and user.is_staff

@login_required
@user_passes_test(staff_check)
def portal_dashboard(request):
    return render(request, 'portal/dashboard.html')


# 🔐 Mixin for class-based staff-only views
class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


# 📝 BlogPost CRUD views

# List all posts
class BlogListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = BlogPost
    template_name = 'blog/list.html'  # ✅ updated path
    context_object_name = 'posts'

# Create new post
class BlogCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/form.html'  # ✅ updated path
    success_url = reverse_lazy('blog_list')

# Edit post
class BlogUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/form.html'  # ✅ updated path
    success_url = reverse_lazy('blog_list')

# Delete post
class BlogDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = BlogPost
    template_name = 'blog/confirm_delete.html'  # ✅ updated path
    success_url = reverse_lazy('blog_list')
