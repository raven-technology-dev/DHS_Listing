from django.contrib import admin
from .models import Club_Representative


class Club_Rep_Admin(admin.ModelAdmin):
    readonly_fields = (
        "representitave_name",
        "club_name",
        "club_description",
        "representative_description",
        "club_is_official",
        "rep_email",
        "rep_phone",
        "agree_to_data_policy",
        "form_submitted_at",
    )


admin.site.register(Club_Representative, Club_Rep_Admin)
