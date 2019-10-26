from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.index, name='index'),  # music/

    path('<int:album_id>/', views.retrieve, name='retrieve'),  # /music/<album_id>/

    path('<int:album_id>/favorite', views.favorite, name='favorite'),  # /music/<album_id>/favorite

]
