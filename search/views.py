from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpRequest
from django.db.models import Q

from .forms import search_form
from listing.models import Club, Event


class search(View):
    """
    This is the View for search queries on this platform. For now,
    this will not have advanced search filters. But eventually,
    this will support search filters.

    This will query:

    - Club Names
    - Event Names
    - People (Sponsors and Leaders) (in Clubs)
    - Organizers (in Events)
    - Emails (in Clubs and Events)

    Search queries should not be case sensitive.

    TODO: Figure out how to order the results.
    """

    def get(self, _request):
        """
        This is the page for is someone enters `/search/` manually.
        This is here mostly to avoid errors if someone sends a GET request to the search page.
        """
        return render(_request, "search/main.html", {})

    def post(self, _request: HttpRequest):
        """
        This is the view that processes search queries, and then redirects users to a "Search reseults" page,
        with the proper context.
        ____
        TODO: Add form validation. For example, if someone sends a phrases query that's more than
        255 char's long, redirect the user to the template for search get requests, but say that their
        search query was too long.
        """
        form = search_form(_request.POST)
        if form.is_valid():
            search_query = form.cleaned_data["phrases"]
            clubs = Club.objects.filter(
                Q(name__icontains=search_query)
                | Q(club_leader__icontains=search_query)
                | Q(club_sponsor__icontains=search_query)
                | Q(email_address__icontains=search_query)
            )
            events = Event.objects.filter(
                Q(event_name__icontains=search_query)
                | Q(organizer_of_event__icontains=search_query)
                | Q(organizer_email__icontains=search_query)
            )
        else:
            pass
            # TODO: Make a page that says there was an issue completing the search query, and to try again.
        if clubs.exists() == False and events.exists() == False:
            # This is a page for no results.
            return render(_request, "search/no_results.html", {})
        return render(
            # This view will render the search results page, as that's the easiest way to do this.
            _request,
            "search/results.html",
            {"clubs": clubs, "events": events},
        )
