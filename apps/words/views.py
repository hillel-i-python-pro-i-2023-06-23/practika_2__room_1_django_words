from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView

from apps.words.models import GameWord
from apps.words.forms import PlayForm
from apps.words.services.save_word import save_word
from apps.words.services.delete_words import delete_words


# Create your views here.
class GameWordsListView(ListView):
    model = GameWord


def GameWordsPlay_view(request):
    if request.method == "POST":
        form = PlayForm(request.POST)

        if form.is_valid():
            word = form.cleaned_data["word"]
            save_word(word=word)

    else:
        form = PlayForm()

    return render(
        request=request,
        template_name="words/gamewords_play.html",
        context=dict(
            gamewords_list=GameWord.objects.all(),
            form=form,
        ),
    )


def delete_words_view(request):
    delete_words()

    return redirect(reverse_lazy("words:gamewords_play"))
