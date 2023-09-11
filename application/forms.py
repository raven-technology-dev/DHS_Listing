from django import forms
from .models import Club_Representative


class Club_Representative_Form(forms.ModelForm):
    agree_to_data_policy = forms.BooleanField(
        required=True,widget=forms.CheckboxInput()
    )
    club_is_official = forms.BooleanField(required=False)

    class Meta:
        model = Club_Representative
        fields = (
            "representitave_name",
            "club_name",
            "club_description",
            "representative_description",
            "club_is_official",
            "rep_email",
            "rep_phone",
            "agree_to_data_policy",
        )
