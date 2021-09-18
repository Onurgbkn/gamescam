from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('games/<slug:slug>/', views.gameplay, name='gameplay'),
]
