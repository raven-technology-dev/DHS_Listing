from django.urls import path
from . import views

urlpatterns = [
    path("",views.search.as_view(),name="search"),
]
