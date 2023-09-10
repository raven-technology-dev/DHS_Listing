from django.shortcuts import render
from django.views import View
from django.http import HttpRequest

from .forms import basic_search_form

# Create your views here.


class search(View):
    def get(self, _request):
        """
        This is the page for is someone enters `/search/` manually.
        This is here mostly to avoid errors if someone sends a GET request to the search page.
        """
    def post(self,_request:HttpRequest):
        """
        This is the view that processes search queries, and then redirects users to a "Search reseults" page,
        with the proper context.
        ____
        TODO: Add form validation. For example, if someone sends a phrases query that's more than
        255 char's long, redirect the user to the template for search get requests, but say that their 
        search query was too long.
        """
        form=basic_search_form(_request.POST)
        if form.is_valid():
            search_query=form.search_phrases
