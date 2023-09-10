from django.shortcuts import render

from .models import Club


def main(_request):
    """
    This is the view for the main listings page.
    """
    return render(_request, "listings/main.html", {})


def clubs_listings(_request):
    """
    This is the view for club listings.
    """
    club_objs = Club.objects.all().order_by("id")
    return render(_request, "listings/clubs/main.html", {"clubs": club_objs})


def club(_request, id: int):
    """
    This is the view for displaying an individual club.
    """
    try:
        club = Club.objects.get(id=id)
    except:
        # This is if a requested club ID does not exist.
        return render(_request, "listings/clubs/club.html", {"club_not_exist": True})
    # If it renders this, the club does exist.
    return render(_request, "listings/clubs/club.html", {"club": club})
