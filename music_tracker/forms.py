from django import forms
from .models import Artist, Song

class SongForm(forms.ModelForm):
    artist_name = forms.CharField(max_length=100, label='Artist')

    class Meta:
        model = Song
        fields = ['title']

    def clean(self):
        cleaned_data = super().clean()
        artist_name = cleaned_data.get('artist_name')

        existing_artist = Artist.objects.filter(name=artist_name).first()
        if not existing_artist:
            existing_artist = Artist.objects.create(name=artist_name)

        cleaned_data['artist'] = existing_artist

        return cleaned_data
