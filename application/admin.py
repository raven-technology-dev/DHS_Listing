from django.contrib import admin
from .models import Club_Representative


class Club_Rep_Admin(admin.ModelAdmin):
    pass


admin.site.register(Club_Representative, Club_Rep_Admin)
