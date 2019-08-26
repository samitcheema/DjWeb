from django.http import HttpResponse
from .models import Albums


def index(request):
    all_albums = Albums.objects.all()
    html = ''
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<a href="' + url + '">' + album.title + '</a><br>'
    return HttpResponse(html)  # added header


def retrieve(request, album_id):
    return HttpResponse("<h2>Album for ID: " + str(album_id) + "</h2>")  # added header
