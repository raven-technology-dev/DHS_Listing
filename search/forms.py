from django import forms

class search_form(forms.Form):
    """
    This is the form used for basic search queries.
    """
    phrases=forms.CharField(label="phrases",max_length=255)
