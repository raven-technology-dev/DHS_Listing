from django.contrib import admin
from .models import Club


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
