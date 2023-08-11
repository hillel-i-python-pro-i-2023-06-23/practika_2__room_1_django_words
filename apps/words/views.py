from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView

from apps.words.models import GameWord, Room
from apps.words.forms import PlayForm
from apps.words.services.save_word import save_word
from apps.words.services.delete_words import delete_words


# Create your views here.
class GameWordsListView(ListView):
    model = GameWord

class RoomListView(ListView):
    model = Room

def GameWordsPlay_view(request, number_of_room=0):
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
            gamewords_list=GameWord.objects.all().filter(numer_of_room=number_of_room),
            form=form,
        ),
    )


def delete_words_view(request):
    delete_words()

    return redirect(reverse_lazy("words:gamewords_play"))

def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'words/room_detail.html', {'room': room})


def other_rooms_list(request, room_id):
    current_room = get_object_or_404(Room, id=room_id)
    other_rooms = Room.objects.exclude(id=room_id)
    return render(request, 'words/other_rooms_list.html', {'current_room': current_room, 'other_rooms': other_rooms})