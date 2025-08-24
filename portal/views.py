# portal/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import logout, get_user_model
from django.http import JsonResponse  # NEW
from django.db.models import Max      # NEW (for auto sort_order)
import json                           # NEW

from blog.models import BlogPost
from flyers.models import Flyer

from .forms import (
    BlogPostForm,
    FlyerForm,
    PortalUserCreateForm,
    PortalUserUpdateForm,
)

from .authz import is_portal_owner, in_group

User = get_user_model()


# staff/owner guard
def staff_check(user):
    return user.is_authenticated and (user.is_staff or is_portal_owner(user))


# Dashboard
@login_required
@user_passes_test(staff_check)
def portal_dashboard(request):
    return render(request, 'portal/dashboard.html')


# Logout
def portal_logout_view(request):
    logout(request)
    messages.success(request, "You have been safely logged out.")
    return redirect('portal:portal_login')


# CBV guard
class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        u = self.request.user
        return u.is_authenticated and (u.is_staff or is_portal_owner(u))


# ===== Owner-only user management =====

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
            return redirect('portal:portal_users')
    else:
        form = PortalUserCreateForm()
    return render(request, "portal/create_user.html", {"form": form})


@login_required
@user_passes_test(is_portal_owner)  # ONLY Leanne (env-driven) can access
def portal_user_edit(request, user_id: int):
    target = get_object_or_404(User, pk=user_id)
    # Safety: never allow deactivating the owner account
    is_target_owner = is_portal_owner(target)

    if request.method == "POST":
        form = PortalUserUpdateForm(request.POST, instance=target)
        if form.is_valid():
            if (
                is_target_owner
                and not form.cleaned_data.get("is_active", True)
            ):
                messages.error(
                    request,
                    "You cannot deactivate the owner account."
                )
            else:
                form.save()
                messages.success(request, "User updated.")
                return redirect('portal:portal_users')
    else:
        form = PortalUserUpdateForm(instance=target)

    return render(
        request,
        "portal/edit_user.html",
        {"form": form, "target": target}
    )


@login_required
@user_passes_test(is_portal_owner)  # ONLY Leanne (env-driven) can access
def portal_user_delete(request, user_id: int):
    target = get_object_or_404(User, pk=user_id)

    # Safety: never delete the owner or yourself
    if is_portal_owner(target):
        messages.error(request, "You cannot delete the owner account.")
        return redirect('portal:portal_users')
    if target.pk == request.user.pk:
        messages.error(request, "You cannot delete your own account.")
        return redirect('portal:portal_users')

    if request.method == "POST":
        username = target.username
        target.delete()
        messages.success(request, f"User '{username}' deleted.")
        return redirect('portal:portal_users')

    # GET → show confirm page
    return render(
        request,
        "portal/confirm_user_delete.html",
        {"target": target}
    )


# ===== Feature gate helper =====
def _require_group_or_redirect(request, group_name: str):
    if not (
        in_group(request.user, group_name) or is_portal_owner(request.user)
    ):
        messages.error(request, "You don't have access to that section.")
        return redirect('portal:portal_dashboard')
    return None


# ===== Blog CRUD (staff/owner + BLOG) =====

class BlogListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = BlogPost
    template_name = 'blog/list.html'
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

    def get_success_url(self):
        return reverse_lazy('portal:blog_edit', kwargs={'pk': self.object.pk})


class BlogUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/form.html'
    success_url = reverse_lazy('portal:blog_list')

    def dispatch(self, request, *args, **kwargs):
        resp = _require_group_or_redirect(request, "BLOG")
        if resp:
            return resp
        return super().dispatch(request, *args, **kwargs)


class BlogDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = BlogPost
    template_name = 'blog/confirm_delete.html'
    success_url = reverse_lazy('portal:blog_list')

    def dispatch(self, request, *args, **kwargs):
        resp = _require_group_or_redirect(request, "BLOG")
        if resp:
            return resp
        return super().dispatch(request, *args, **kwargs)


# ===== Flyers CRUD (staff/owner + FLYERS) =====

class FlyerListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = Flyer
    template_name = 'flyers/flyers_list.html'
    context_object_name = 'flyers'

    def dispatch(self, request, *args, **kwargs):
        resp = _require_group_or_redirect(request, "FLYERS")
        if resp:
            return resp
        return super().dispatch(request, *args, **kwargs)

    # Respect manual ordering in portal too
    def get_queryset(self):
        return Flyer.objects.order_by("sort_order", "event_date")


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

    # Ensure uploaded files are passed to the form
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["files"] = self.request.FILES or None
        return kwargs

    # Print real validation errors so we can see why it failed
    def form_invalid(self, form):
        print("=== FLYER CREATE INVALID ===")
        print("METHOD:", self.request.method)
        print("CONTENT_TYPE:", self.request.META.get("CONTENT_TYPE"))
        print("FILES KEYS:", list(self.request.FILES.keys()))
        print("POST KEYS:", list(self.request.POST.keys()))
        print("FORM ERRORS JSON:", form.errors.as_json())
        return super().form_invalid(form)

    # Set sort_order automatically and save cleanly (no double-save)
    def form_valid(self, form):
        obj = form.save(commit=False)

        # Auto-append to the end of the list
        max_order = Flyer.objects.aggregate(m=Max("sort_order"))["m"]
        obj.sort_order = (max_order + 1) if max_order is not None else 0

        obj.save()
        form.save_m2m()
        self.object = obj  # tell the CBV what we saved

        img = getattr(obj, "image", None)
        print("=== FLYER CREATED ===", obj.pk,
              getattr(img, "name", None),
              getattr(img, "url", None))
        return redirect(self.get_success_url())


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

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["files"] = self.request.FILES or None
        return kwargs

    def form_invalid(self, form):
        print("=== FLYER UPDATE INVALID ===")
        print("METHOD:", self.request.method)
        print("CONTENT_TYPE:", self.request.META.get("CONTENT_TYPE"))
        print("FILES KEYS:", list(self.request.FILES.keys()))
        print("POST KEYS:", list(self.request.POST.keys()))
        print("FORM ERRORS JSON:", form.errors.as_json())
        return super().form_invalid(form)

    # Save using the parent, then print what changed
    def form_valid(self, form):
        response = super().form_valid(form)
        obj = self.object
        img = getattr(obj, "image", None)
        print("=== FLYER UPDATED ===", obj.pk,
              getattr(img, "name", None),
              getattr(img, "url", None))
        return response


class FlyerDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Flyer
    template_name = 'flyers/flyer_confirm_delete.html'
    success_url = reverse_lazy('portal:flyer_list')

    def dispatch(self, request, *args, **kwargs):
        resp = _require_group_or_redirect(request, "FLYERS")
        if resp:
            return resp
        return super().dispatch(request, *args, **kwargs)


# ===== Flyers drag-and-drop reorder (NEW) =====

@login_required
def flyers_reorder(request):
    # same feature gate as other flyers views
    resp = _require_group_or_redirect(request, "FLYERS")
    if resp:
        return resp

    # AJAX POST with array of IDs → save new sort_order
    if (
        request.method == "POST"
        and request.headers.get("x-requested-with") == "XMLHttpRequest"
    ):
        try:
            data = json.loads(request.body.decode("utf-8"))
            order = data.get("order", [])
            for idx, flyer_id in enumerate(order):
                Flyer.objects.filter(pk=flyer_id).update(sort_order=idx)
            return JsonResponse({"ok": True})
        except Exception as e:
            return JsonResponse({"ok": False, "error": str(e)}, status=400)

    # GET → render the reorder UI
    flyers = Flyer.objects.order_by("sort_order", "event_date")
    return render(request, "flyers/reorder.html", {"flyers": flyers})
