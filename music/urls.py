from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),  # music/

    path('<int:pk>/', views.RetrieveView.as_view(), name='retrieve'),  # /music/<album_id>/

    path('album/add/', views.AlbumCreate.as_view(), name='album-add')   # /music/album/add/


]
