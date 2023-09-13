from django.contrib import admin
from .models import Representative_Application


class Rep_Admin(admin.ModelAdmin):
    readonly_fields = (
        "representitave_name",
        "thing_name",
        "thing_description",
        "representative_description",
        "thing_is_official",
        "rep_email",
        "rep_phone",
        "agree_to_data_policy",
        "form_submitted_at",
    )


admin.site.register(Representative_Application, Rep_Admin)
