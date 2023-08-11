from django import forms

from apps.words.models import GameWord


class PlayForm(forms.Form):
    word = forms.CharField(
        label="word",
        required=True,
    )

    class Meta:
        model = GameWord

        fieldsets = ("name_of_gamer", "word")
