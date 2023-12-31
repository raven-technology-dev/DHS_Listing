"""
URL configuration for DHS_Listings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

admin.site.name="Dimond HS Listings"
admin.site.site_title="Dimond HS Listings"
admin.site.index_title="Staff Panel"
admin.site.site_header="Dimond HS Listings Staff"

urlpatterns = [
    path("admin/doc/", include("django.contrib.admindocs.urls")),
    path("admin/", admin.site.urls),
    path("", include("homepage.urls")),
    path("search/", include("search.urls")),
    path("about/", include("about.urls")),
    path("listings/", include("listing.urls")),
    path("applications/", include("application.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
