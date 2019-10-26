# import csv, io
from django.shortcuts import render, get_object_or_404
from .models import Albums, Song


def index(request):
    all_albums = Albums.objects.all()
    context = {
        'all_albums': all_albums,
    }
    return render(request, 'music/index.html', context)


def retrieve(request, album_id):
    album = get_object_or_404(Albums, pk=album_id,)
    return render(request, 'music/retrieve.html', {'album': album})


def favorite(request, album_id):
    album = get_object_or_404(Albums, pk=album_id,)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/retrieve.html', {
            'album': album,
            'error message': "You did not select a valid song.",
        })
    else:
        selected_song.favorite = True
        selected_song.save()
        return render(request, 'music/retrieve.html', {'album': album})


