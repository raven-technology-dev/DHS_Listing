from django.urls import path
from . import views

app_name = "Listing"

urlpatterns = [
    path("", views.main, name="listing"),
    path("clubs/", views.clubs_listings, name="clubs"),
    path("clubs/<id>", views.club),
    path("events/", views.events_listings, name="events"),
    path("events/<id>", views.event),
    path("events/past/",views.past_events,name="past_events"),
]
