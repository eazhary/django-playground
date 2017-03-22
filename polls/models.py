from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Album(models.Model):

    title = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    artist = models.ForeignKey(Artist)

    def __str__(self):
        return self.title + " " + self.artist.name

class Song(models.Model):

    title = models.CharField(max_length=50)
    album = models.ForeignKey(Album)

    def __str__(self):
        return self.title

