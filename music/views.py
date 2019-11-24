from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Albums


class IndexView(generic.ListView):
    template_name = 'music/index.html'

    def get_queryset(self):
        return Albums.objects.all()


class RetrieveView(generic.DetailView):
    model = Albums
    template_name = 'music/retrieve.html'


class AlbumCreate(CreateView):
    model = Albums
    fields = ['name', 'title', 'genre', 'year', 'record_label']
    template_name = 'music/album_form.html'


class AlbumUpdate(UpdateView):
    model = Albums
    fields = ['name', 'title', 'genre', 'year', 'record_label']
    template_name = 'music/album_form.html'


class AlbumDelete(DeleteView):
    model = Albums
    success_url = reverse_lazy('music:index')
    fields = ['name', 'title', 'genre', 'year', 'record_label']
    template_name = 'music/album_form.html'
