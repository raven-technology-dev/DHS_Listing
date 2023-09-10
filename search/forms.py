from django import forms

class basic_search_form(forms.Form):
    """
    This is the form used for basic search queries.
    """
    search_phrases=forms.CharField(label="phrases",max_length=255)
