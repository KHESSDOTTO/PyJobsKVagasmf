from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from pyjobs.marketing.forms import SharingForm
from pyjobs.core.models import Job


@login_required
def sharing_job_view(request, unique_slug):
    context = {
        "job": get_object_or_404(Job, unique_slug=unique_slug),
        "logged_in": False,
    }

    context["title"] = context["job"].title
    context["description"] = context["job"].description
    context["form"] = SharingForm(request.POST or None)

    is_valid_before = context["form"].is_valid()

    if request.method == "POST" and context["form"].is_valid():
        context["form"].save(user_sharing=request.user, job=context["job"])
        context["shared"] = True
        context["form"] = SharingForm(None)

    if request.method == "POST" and not is_valid_before:
        context["invalid_email"] = True
        context["form"] = SharingForm(None)

    return render(request, template_name="job_sharing.html", context=context)
