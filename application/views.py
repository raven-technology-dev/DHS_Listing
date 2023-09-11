from django.shortcuts import render
from django.views import View
from .forms import Club_Representative_Form


def main(_request):
    """"""
    return render(_request, "application/main.html", {})


class club_representaive_application(View):
    """
    This is the view that serves Club Representative Applcations.
    """

    def get(self, _request):
        return render(_request, "application/club_representative.html", {})

    def post(self, _request):
        form = Club_Representative_Form(_request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            print(form.errors.as_data())
            # TODO: Make this return an error page, using the same template. Allow the user another chance to redo the form.
            pass  # For now.
        return render(_request, "application/club_representative.html", {"form":form})
        # TODO: If user didn't agree to Data Processing Policy, return with that message.
        # TODO: If form is all good redirect to page that says that the form was submitted.
