from django.views import generic
from .models import Albums


class IndexView(generic.ListView):
    template_name = 'music/index.html'

    def get_queryset(self):
        return Albums.objects.all()


class RetrieveView(generic.DetailView):
    model = Albums
    template_name = 'music/retrieve.html'
