from django.shortcuts import render


def main(_request):
    """
    The view for the main about page.
    """
    return render(_request, "about/main.html", {})


def terms_of_service(_request):
    """
    This is the view that render's our terms of service.
    """
    return render(_request, "about/terms_of_service.html", {})


def privacy_policy(_request):
    """
    This is the view that render's our privacy policy.
    """
    return render(_request, "about/privacy_policy.html", {})


def data_processing_policy(_request):
    """
    This is the view that render's our data processing policy.
    """
    return render(_request, "about/data_processing_policy.html", {})
