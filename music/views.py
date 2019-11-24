from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from .models import Albums
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'music/index.html'

    def get_queryset(self):
        return Albums.objects.all()


class RetrieveView(generic.DetailView):
    model = Albums
    template_name = 'music/retrieve.html'


class AlbumCreate(CreateView):
    model = Albums
    fields = ['name', 'title', 'genre', 'year', 'record_label', 'logo']
    template_name = 'music/album_form.html'


class AlbumUpdate(UpdateView):
    model = Albums
    fields = ['name', 'title', 'genre', 'year', 'record_label', 'logo']
    template_name = 'music/album_form.html'


class AlbumDelete(DeleteView):
    model = Albums
    success_url = reverse_lazy('music:index')
    fields = ['name', 'title', 'genre', 'year', 'record_label', 'logo']
    template_name = 'music/album_form.html'


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    def get(self, request):  # display blank registration form
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):  # process the form
        form = self.form_class(request.POST)

        if form.is_valid():  # if the form is valid
            user = form.save(commit=False)  # stored locally

            username = form.cleaned_data['username']  # legitimize the data
            password = form.cleaned_data['password']
            user.set_password(password)  # set the password
            user.save()

            user = authenticate(username=username,
                                password=password)  # authenticate username and pass to see if they are in database

            if user is not None:

                if user.is_active:
                    login(request, user)  # user is now logged in
                    return redirect('music:index')  # redirect user to index page

            return render(request, self.template_name, {'form': form})  # send user back to blank form


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'music/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Albums.objects.filter(user=request.user)
                return render(request, 'music/index.html', {'albums': albums})
            else:
                return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'music/login.html', {'error_message': 'Invalid login'})
    return render(request, 'music/login.html')
