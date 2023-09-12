from django.urls import path
from . import views

app_name = "About"

urlpatterns = [
    path("", views.main, name="about"),
    path("terms_of_service/", views.terms_of_service, name="terms_of_service"),
    path("privacy_policy/", views.privacy_policy, name="privacy_policy"),
    path(
        "data_processing_policy/",
        views.data_processing_policy,
        name="data_processing_policy",
    ),
]
