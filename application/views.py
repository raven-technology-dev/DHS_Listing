from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import Representative_Form


def main(_request):
    """"""
    return render(_request, "application/main.html", {})


class representative_application(View):
    """
    This is the view that serves Representative Applications.
    """

    def get(self, _request):
        return render(_request, "application/representative.html", {})

    def post(self, _request):
        form = Representative_Form(_request.POST)
        if form.is_valid():
            form.save()
        else:
            # NOTE: If user didn't agree to Data Processing Policy, this will return with that message.
            return render(_request, "application/representative.html", {"form": form})
        return redirect(reverse("Application:representative_appl_subm"))
        # NOTE: If form was all good, this will redirect to page that says that the form was submitted.


def rep_appl_submitted(_request):
    """
    This is the view for when Representative Applications were submitted successfully.
    """
    return render(_request, "application/representative_success.html", {})
