from django.urls import path
from . import views

app_name = "Application"

urlpatterns = [
    path("", views.main),
    path(
        "representative/",
        views.representative_application.as_view(),
        name="representative",
    ),
    path(
        "representative_appl_subm/",
        views.rep_appl_submitted,
        name="representative_appl_subm",
    ),
]
