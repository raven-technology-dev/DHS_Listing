from django.shortcuts import render
from django.utils.timezone import now

from .models import Club, Event


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
        # TODO: make a specialized page for club not exist.
        return render(_request, "listings/clubs/club.html", {"club_not_exist": True})
    # If it renders this, the club does exist.
    return render(_request, "listings/clubs/club.html", {"club": club})


def events_listings(_request):
    """
    This is the view for event listings.
    """
    # refrernce: https://stackoverflow.com/questions/45947222/django-queryset-with-datetime-need-to-get-all-future-dated-entries
    event_objs = Event.objects.filter(date_time_of_event__gte=now()).order_by(
        "date_time_of_event"
    )
    return render(_request, "listings/events/main.html", {"events": event_objs})


def event(_request, id: int):
    """
    This is the view for rendering an individual event.
    """
    try:
        event = Event.objects.get(id=id)
    except:
        # TODO: make a specialized page for event not exist.
        return render(_request, "listings/events/event.html", {"club_not_exist": True})
    if now() > event.date_time_of_event:
        already_happened = True
    else:
        already_happened = False
    return render(
        _request,
        "listings/events/event.html",
        {"event": event, "already_happened": already_happened},
    )


def past_events(_request):
    """
    This is the view that renders the menu of past events.
    """
    event_objs = Event.objects.filter(date_time_of_event__lte=now()).order_by(
        "-date_time_of_event"
    )
    return render(_request, "listings/events/past.html", {"events": event_objs})
