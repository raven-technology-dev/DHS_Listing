from django.urls import path
from . import views

app_name = "Home-page"

urlpatterns = [
    path("", views.homepage, name="homepage"),
]
