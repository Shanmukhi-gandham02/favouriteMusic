from django.shortcuts import render, redirect
from .models import Song, Artist
from .forms import SongForm

# Create your views here.

def songList(request):
    allSongs = Song.objects.all()
    return render(request, 'music_tracker/song_list.html', {'allSongs': allSongs})


def songDetail(request, id):
    song = Song.objects.get(pk=id)
    return render(request, 'music_tracker/song_detail.html', {'song': song})

def addSong(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save(commit=False)

            # Set the artist field manually
            song.artist = form.cleaned_data['artist']
            song.save()
            return redirect('song-list')
    else:
        form = SongForm()
    return render(request, 'music_tracker/add_song.html', {'form': form})


def artistList(request):
    artists = Artist.objects.all()
    return render(request, 'music_tracker/artist_list.html', {'artists': artists})
