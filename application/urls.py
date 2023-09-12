from django.urls import path
from . import views

app_name = "Application"

urlpatterns = [
    path("", views.main),
    path(
        "club_representative/",
        views.club_representaive_application.as_view(),
        name="club_representative",
    ),
    path(
        "club_representative_appl_subm/",
        views.club_rep_appl_submitted,
        name="club_representative_appl_subm",
    ),
]
