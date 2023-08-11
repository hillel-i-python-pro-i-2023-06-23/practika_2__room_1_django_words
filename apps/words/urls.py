from django.urls import path

from . import views

app_name = "words"

urlpatterns = [
    # path("list/", views.GameWordsListView.as_view(), name="gamewords_list"),
    #
    # path("delete/", views.delete_contacts_view, name="words_delete"),
    #
    #path("play/", views.GameWordsPlay_view, name="gamewords_play"),
    #
    #path("delete/", views.delete_words_view, name="gamewords_delete"),
    # path("room/<int:room_id>/", views.room_detail_views, name="room_detail"),

    path("room_detail/", views.delete_words_view, name="gamewords_delete"),

    path('room/<int:room_id>/other-rooms/', views.other_rooms_list, name='other_rooms_list')
]
