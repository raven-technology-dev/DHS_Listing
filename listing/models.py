from django.db import models


class Club(models.Model):
    """
    This is the Model that hold the info for clubs.
    """

    name = models.CharField(
        verbose_name="Name of Club",
        max_length=50,
        help_text="This field hold the name of your club.",
    )
    thumbnail_image = models.ImageField(
        verbose_name="Club Thumbnail Image",
        help_text="This image is the image best used to represent this club.",
        null=True,
        blank=True,
        upload_to="clubs/thumbnails/",
    )
    club_leader = models.CharField(
        verbose_name="Club Leader",
        help_text="Name of the owner or leader of this club.",
        max_length=75,
    )
    club_sponsor = models.CharField(
        verbose_name="Club Sponsor",
        max_length=75,
        help_text="This field is optional. Name of the sponsor of this club.",
        null=True,
        blank=True,
    )
    is_official = models.BooleanField(
        verbose_name="Club is official",
        default=True,
        help_text="If this club is officially endorsed or recognized by Dimond HS.",
    )
    member_amount = models.IntegerField(
        verbose_name="Member Count",
        null=True,
        blank=True,
        help_text="This field is optional. The amount of members in this club.",
    )
    phone_number = models.CharField(
        verbose_name="Phone Number for club",
        null=True,
        blank=True,
        max_length=50,
        help_text="This field is optional. A relevant phone number for this club that people can call.",
    )
    email_address = models.EmailField(
        verbose_name="Email for Club",
        help_text="A relevant email address for this club.",
    )
    regular_meeting_time = models.CharField(
        max_length=255,
        verbose_name="Club Meeting times",
        help_text="This field is the meeting time(s) for this club. Feel free to input multiple, just make sure to seperate them all. Please input proper sentences, including punctuation.",
    )
    regular_meeting_location = models.CharField(
        max_length=255,
        verbose_name="Club Meeting location",
        help_text="This field is the location where this club usually meets during regular times. Please input proper sentences, including punctuation.",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="If club is active",
        help_text="This is if the club is currently active. This defaults to true.",
    )
    is_accepting_new_members = models.BooleanField(
        default=True,
        verbose_name="If club is accepting new members",
        help_text="Is the club is currently accepting new members. This defaults to true.",
    )
    club_short_description = models.TextField(
        max_length=255,
        verbose_name="Short Description",
        help_text="This is the short description of this club, so users can see what your club is from the club menu.",
    )
    club_description = models.TextField(
        verbose_name="Club Description", help_text="Description of this club."
    )
    notes = models.TextField(
        verbose_name="Any notes or disclosures for this club",
        help_text="This field is optional. This field is for if you feel that anything needs to be noted for this club.",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Club Listing"
        verbose_name_plural = "Club Listings"

    def __str__(self) -> str:
        return f"{self.name}"


class Event(models.Model):
    """
    This is the model for an Event listing on this platform.
    """

    # TODO: On events listing menu, have only upcoming events be shown.
    # But, have a way that the user could see listings of past events.
    event_name = models.CharField(max_length=255, verbose_name="Name of this event")
    # TODO: thumbnail image.
    thumbnail_image = models.ImageField(
        verbose_name="Event Thumbnail Image",
        help_text="This image is the image best used to represent this event.",
        null=True,
        blank=True,
        upload_to="events/thumbnails/",
    )
    organizer_of_event = models.CharField(
        max_length=255,
        verbose_name="Event Organizer",
        help_text="Person or Club holding the Event.",
    )
    date_time_of_event = models.DateTimeField(verbose_name="Date and Time of the event")
    location_of_event = models.CharField(
        max_length=255, verbose_name="Location of the Event"
    )
    event_short_description = models.TextField(
        max_length=255,
        verbose_name="Short Description of the Event",
        help_text="This should be a short description of the event. This is needed so people can see what the event is, without having to read a lot.",
    )
    event_description = models.TextField(
        verbose_name="Description of the Event",
        help_text="This should be the long description of the event.",
    )
    organizer_email = models.EmailField(
        verbose_name="Email Address",
        help_text="Email of the event organizer, so people can contact organizer if needed.",
    )
    organizer_phone_number = models.CharField(
        verbose_name="Phone Number",
        null=True,
        blank=True,
        max_length=50,
        help_text="This field is optional. A relevant phone number for the organizer, so they can make contact if needed.",
    )
    is_official = models.BooleanField(
        default=False,
        verbose_name="Is Official",
        help_text="If this event is officially endorsed by Dimond High School.",
    )

    class Meta:
        verbose_name = "Event Listing"
        verbose_name_plural = "Events Listings"

    def __str__(self) -> str:
        return f"{self.event_name} by {self.organizer_of_event}"
