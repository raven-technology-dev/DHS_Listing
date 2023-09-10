from django.urls import path
from . import views

app_name = "Listing"

urlpatterns = [
    path("", views.main, name="listing"),
    path("clubs/", views.clubs_listings, name="clubs"),
    path("clubs/<id>", views.club),
]
