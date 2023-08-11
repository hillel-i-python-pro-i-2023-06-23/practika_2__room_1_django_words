# Create your models here.
from django.db import models


class GameWord(models.Model):
    # Name
    name_of_gamer = models.CharField(max_length=100)
    # Optional phone number
    # phone_number = PhoneNumberField(blank=True)
    word = models.CharField(max_length=40, blank=False)

    number_of_room = models.IntegerField(default=0, blank=True)

    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
    )

    def __str__(self):
        return f"{self.name_of_gamer} {self.word}"

    class Meta:
        ordering = ["number_of_room", "-created_at", "name_of_gamer"]
