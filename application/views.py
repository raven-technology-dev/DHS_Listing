from django.shortcuts import render,redirect
from django.urls import reverse
from django.views import View
from .forms import Club_Representative_Form


def main(_request):
    """"""
    return render(_request, "application/main.html", {})


class club_representaive_application(View):
    """
    This is the view that serves Club Representative Applications.
    """

    def get(self, _request):
        return render(_request, "application/club_representative.html", {})

    def post(self, _request):
        form = Club_Representative_Form(_request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(
                _request, "application/club_representative.html", {"form": form}
            )
        return redirect(reverse("Application:club_representative_appl_subm"))
        # TODO: If user didn't agree to Data Processing Policy, return with that message.
        # TODO: If form is all good redirect to page that says that the form was submitted.


def club_rep_appl_submitted(_request):
    """
    This is the view for when Club Representative Applications were submitted successfully.
    """
    return render(_request, "application/club_representative_success.html", {})
