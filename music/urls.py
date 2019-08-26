from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # music/
    path('<int:album_id>/', views.retrieve, name='retrieve'),  # /music/id#/
]
