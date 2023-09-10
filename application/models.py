from django.db import models

# Create your models here.


class Club_Representative(models.Model):
    """
    This is the data model for Club Representative applications.
    """

    representitave_name = models.CharField(
        verbose_name="Representitave Name",
        max_length=75,
        help_text="Name of the Representative.",
    )
    club_name = models.CharField(
        verbose_name="Name of Club",
        max_length=75,
        help_text="Name of the Club.",
    )
    club_description = models.TextField(
        verbose_name="Club Description",
        help_text="Description of the Club.",
    )
    representitave_description = models.TextField(
        verbose_name="Representitave Description",
        help_text="Description of what the representitave does for the club.",
    )
    club_is_official = models.BooleanField(
        default=False,
        verbose_name="If club is official",
        help_text="If the club is officially endorsed bu Dimond HS.",
    )
    rep_email = models.EmailField(
        verbose_name="Email for Representitave", help_text="Email for the applicant."
    )
    rep_phone = models.CharField(
        max_length=50,
        verbose_name="Phone for Representitave",
        help_text="Phone number for the applicant.",
    )
    agree_to_data_policy = models.BooleanField(
        default=False,
        verbose_name="Agreement to Data Policy",
        help_text="If the applicant agrees to RT's data processing policy. This agreement is REQUIRED for submitting an application.",
    )
    form_submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Club Representitave Application"
        verbose_name_plural = "Club Representitave Applications"

    def __str__(self) -> str:
        return f"{self.representitave_name}"
