from django.urls import path
from . import views

urlpatterns = [
    path('', views.getMusicData),
    path('add/', views.addMusicData),
    path('dummy/', views.getDummyData),
]