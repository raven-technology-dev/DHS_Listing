from django.contrib import admin
from .models import Club, Event


class ClubAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "email_address",
    ]
    search_fields = [
        "name",
        "club_leader",
        "email_address",
    ]
    list_filter = [
        "is_official",
    ]


admin.site.register(
    Club,
    ClubAdmin,
)


class EventAdmin(admin.ModelAdmin):
    list_display = ["event_name", "organizer_of_event", "date_time_of_event"]
    search_fields = [
        "date_time_of_event",
        "event_name",
        "organizer_of_event",
        "organizer_email",
        "location_of_event",
    ]
    list_filter = ["is_official"]


admin.site.register(Event, EventAdmin)
