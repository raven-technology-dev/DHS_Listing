from django.shortcuts import render


def main(_request):
    """
    The view for the main about page.
    """
    return render(_request, "about/main.html", {})
