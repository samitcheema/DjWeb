from django.db import models


class Albums(models.Model):
    name = models.CharField(max_length=100, default='')  # name of artist
    title = models.CharField(max_length=100, default='')  # title of album
    genre = models.CharField(max_length=50, default='')  # genre of album
    logo = models.CharField(max_length=1000, default='')  # album logo
    year = models.CharField(max_length=4, default='')  # album year
    record_label = models.CharField(max_length=100, default='')  # record label

    def __str__(self):
        return 'Artist: ' + self.name + ' Album title: ' + self.title


class Song(models.Model):
    album = models.ForeignKey(Albums, on_delete=models.CASCADE)  # song album, on deletion delete all reference to song.
    format = models.CharField(max_length=10, default='')  # file type, i.e. mp4
    song_title = models.CharField(max_length=100, default='')  # song title
    duration = models.CharField(max_length=100, default='')  # song duration
