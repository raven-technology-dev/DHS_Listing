from django import forms
from .models import Representative_Application


class Representative_Form(forms.ModelForm):
    agree_to_data_policy = forms.BooleanField(
        required=True, widget=forms.CheckboxInput()
    )
    club_is_official = forms.BooleanField(required=False)

    class Meta:
        model = Representative_Application
        fields = (
            "representitave_name",
            "thing_name",
            "thing_description",
            "representative_description",
            "thing_is_official",
            "rep_email",
            "rep_phone",
            "agree_to_data_policy",
        )
