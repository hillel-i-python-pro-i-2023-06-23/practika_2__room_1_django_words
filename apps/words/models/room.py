from django.db import models

class Room(models.Model):
    # Name
    name_of_room = models.CharField(max_length=100)
    number_of_room = models.IntegerField(blank=False)

    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
    )

    def __str__(self):
        return f"#{self.number_of_room} {self.name_of_room}"

    class Meta:
        ordering = ["-created_at", "number_of_room"]
