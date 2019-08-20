from django.db import models


class Albums(models.Model):
    name = models.CharField(max_length=100)  # name of album
    title = models.CharField(max_length=100)  # title of album
    genre = models.CharField(max_length=50)  # genre of album
    logo = models.CharField(max_length=1000)  # album logo
    year = models.CharField(max_length=4)  # album year
    record_label = models.CharField(max_length=100)  # record label


class Song(models.Model):
    album = models.ForeignKey(Albums, on_delete=models.CASCADE)  # song album, on deletion delete all reference to song.
    format = models.CharField(max_length=10)  # file type, i.e. mp4
    song_title = models.CharField(max_length=100)  # song title
    duration = models.CharField(max_length=100)  # song duration
