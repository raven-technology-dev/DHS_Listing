from django.db import models

# Create your models here.


class Representative_Application(models.Model):
    """
    This is the data model for both `Club Representative` and `Event Representative` applications.
    """

    representitave_name = models.CharField(
        verbose_name="Representitave Name",
        max_length=75,
        help_text="Name of the Representative.",
    )
    thing_name = models.CharField(
        verbose_name="Name of Club or event",
        max_length=75,
        help_text="Name of the Club or Event that you are representing.",
    )
    thing_description = models.TextField(
        verbose_name="Description or Club or Event",
        help_text="Description of what you do for the Club or Event.",
    )
    representative_description = models.TextField(
        verbose_name="Representitave Description",
        help_text="Description of what you do for the club or event.",
    )
    thing_is_official = models.BooleanField(
        default=False,
        verbose_name="If club or event is official",
        help_text="If the club or event is officially endorsed by Dimond HS.",
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
        help_text="If the applicant agrees to RT's ToS and Privacy Policy. This agreement is REQUIRED for submitting an application.",
    )
    form_submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Representitave Application"
        verbose_name_plural = "Representitave Applications"

    def __str__(self) -> str:
        return f"{self.representitave_name} for {self.thing_name}"
