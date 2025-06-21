ffrom django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

def staff_check(user):
    return user.is_authenticated and user.is_staff

@login_required
@user_passes_test(staff_check)
def portal_dashboard(request):
    return render(request, 'portal/dashboard.html')
rom django.shortcuts import render

# Create your views here.
