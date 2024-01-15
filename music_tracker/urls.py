from django.urls import path
from .views import songList,songDetail, addSong, artistList

urlpatterns = [
    path('', songList, name="song-list"),
    path('songs/<int:id>/', songDetail, name="song-detail"),
    path('add/', addSong, name='add-song'),
    path('artists/', artistList, name='artist-list' ),
]