# portal/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import logout, get_user_model

from blog.models import BlogPost
from flyers.models import Flyer

from .forms import BlogPostForm, FlyerForm, PortalUserCreateForm  # NEW
from .authz import is_portal_owner, in_group  # NEW

User = get_user_model()


# 🔐 Function-based staff access check for dashboard
def staff_check(user):
    return user.is_authenticated and user.is_staff

# ──────────────────────────────────────────────────────────────────────────────
# Portal LOGIN views
# ──────────────────────────────────────────────────────────────────────────────


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

# ──────────────────────────────────────────────────────────────────────────────
# OWNER-ONLY: Users list + Create user (checkboxes for BLOG/SCHEDULE/FLYERS)
# ──────────────────────────────────────────────────────────────────────────────


@login_required
@user_passes_test(is_portal_owner)  # ONLY Leanne (env-driven) can access
def portal_users_list(request):
    users = User.objects.order_by('username').all()
    return render(request, "portal/users_list.html", {"users": users})


@login_required
@user_passes_test(is_portal_owner)  # ONLY Leanne (env-driven) can access
def portal_user_create(request):
    if request.method == "POST":
        form = PortalUserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully.")
            return redirect('portal:portal_dashboard')
    else:
        form = PortalUserCreateForm()
    return render(request, "portal/create_user.html", {"form": form})

# ──────────────────────────────────────────────────────────────────────────────
# FEATURE GATE helper (BLOG / SCHEDULE / FLYERS)
# ──────────────────────────────────────────────────────────────────────────────


def _require_group_or_redirect(request, group_name: str):
    """
    If the signed-in user is not in the required feature group,
    flash a message and send them back to the dashboard.
    """
    if not in_group(request.user, group_name):
        messages.error(request, "You don't have access to that section.")
        return redirect('portal:portal_dashboard')
    return None

# ──────────────────────────────────────────────────────────────────────────────
# 📝 BlogPost CRUD views (require staff + BLOG feature)
# ──────────────────────────────────────────────────────────────────────────────


class BlogListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = BlogPost
    template_name = 'blog/list.html'  # backend management list
    context_object_name = 'posts'

    def dispatch(self, request, *args, **kwargs):
        resp = _require_group_or_redirect(request, "BLOG")
        if resp:
            return resp
        return super().dispatch(request, *args, **kwargs)


class BlogCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/form.html'

    def dispatch(self, request, *args, **kwargs):
        resp = _require_group_or_redirect(request, "BLOG")
        if resp:
            return resp
        return super().dispatch(request, *args, **kwargs)

    # After creating, go straight to the edit page for the new post
    def get_success_url(self):
        return reverse_lazy('portal:blog_edit', kwargs={'pk': self.object.pk})


class BlogUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/form.html'
    # After saving edits, return to the portal list
    success_url = reverse_lazy('portal:blog_list')

    def dispatch(self, request, *args, **kwargs):
        resp = _require_group_or_redirect(request, "BLOG")
        if resp:
            return resp
        return super().dispatch(request, *args, **kwargs)


class BlogDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = BlogPost
    template_name = 'blog/confirm_delete.html'
    # After deletion, return to the portal list
    success_url = reverse_lazy('portal:blog_list')

    def dispatch(self, request, *args, **kwargs):
        resp = _require_group_or_redirect(request, "BLOG")
        if resp:
            return resp
        return super().dispatch(request, *args, **kwargs)


# ──────────────────────────────────────────────────────────────────────────────
# 🖼 Flyers CRUD views (require staff + FLYERS feature)
# ──────────────────────────────────────────────────────────────────────────────
class FlyerListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = Flyer
    template_name = 'flyers/flyers_list.html'
    context_object_name = 'flyers'

    def dispatch(self, request, *args, **kwargs):
        resp = _require_group_or_redirect(request, "FLYERS")
        if resp:
            return resp
        return super().dispatch(request, *args, **kwargs)


class FlyerCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Flyer
    form_class = FlyerForm
    template_name = 'flyers/flyer_form.html'
    success_url = reverse_lazy('portal:flyer_list')

    def dispatch(self, request, *args, **kwargs):
        resp = _require_group_or_redirect(request, "FLYERS")
        if resp:
            return resp
        return super().dispatch(request, *args, **kwargs)


class FlyerUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Flyer
    form_class = FlyerForm
    template_name = 'flyers/flyer_form.html'
    success_url = reverse_lazy('portal:flyer_list')

    def dispatch(self, request, *args, **kwargs):
        resp = _require_group_or_redirect(request, "FLYERS")
        if resp:
            return resp
        return super().dispatch(request, *args, **kwargs)


class FlyerDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Flyer
    template_name = 'flyers/flyer_confirm_delete.html'
    success_url = reverse_lazy('portal:flyer_list')

    def dispatch(self, request, *args, **kwargs):
        resp = _require_group_or_redirect(request, "FLYERS")
        if resp:
            return resp
        return super().dispatch(request, *args, **kwargs)
