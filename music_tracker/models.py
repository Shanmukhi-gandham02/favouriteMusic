from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def song_count(self):
        return self.song_set.count()
    
class Song(models.Model):
    title = models.CharField(max_length=250)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.artist}'s song - {self.title}"
    
    
