from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import logout

from blog.models import BlogPost
from .forms import BlogPostForm

from flyers.models import Flyer
from .forms import FlyerForm


# 🔐 Function-based staff access check for dashboard
def staff_check(user):
    return user.is_authenticated and user.is_staff


# Portal LOGIN views
@login_required
@user_passes_test(staff_check)
def portal_dashboard(request):
    return render(request, 'portal/dashboard.html')


# Portal LOGOUT view
def portal_logout_view(request):
    logout(request)
    messages.success(request, "You have been safely logged out.")
    # Use namespaced URL so it resolves under /portal/
    return redirect('portal:portal_login')


# 🔐 Mixin for class-based staff-only views
class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


# 📝 BlogPost CRUD views

# List all posts (portal management)
class BlogListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = BlogPost
    template_name = 'blog/list.html'  # backend management list
    context_object_name = 'posts'


# Create new post
class BlogCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/form.html'

    # After creating, go straight to the edit page for the new post
    def get_success_url(self):
        return reverse_lazy('portal:blog_edit', kwargs={'pk': self.object.pk})


# Edit post
class BlogUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/form.html'
    # After saving edits, return to the portal list
    success_url = reverse_lazy('portal:blog_list')


# Delete post
class BlogDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = BlogPost
    template_name = 'blog/confirm_delete.html'
    # After deletion, return to the portal list
    success_url = reverse_lazy('portal:blog_list')


# 🖼 Flyers views
class FlyerListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = Flyer
    template_name = 'flyers/flyers_list.html'
    context_object_name = 'flyers'


class FlyerCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Flyer
    form_class = FlyerForm
    template_name = 'flyers/flyer_form.html'
    success_url = reverse_lazy('portal:flyer_list')


class FlyerUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Flyer
    form_class = FlyerForm
    template_name = 'flyers/flyer_form.html'
    success_url = reverse_lazy('portal:flyer_list')


class FlyerDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Flyer
    template_name = 'flyers/flyer_confirm_delete.html'
    success_url = reverse_lazy('portal:flyer_list')
