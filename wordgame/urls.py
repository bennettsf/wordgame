from django.urls import path
from . import views

#URL configuration module (URLConf)
urlpatterns = [
    path('', views.wordgame, name="wordgame"),
    path('fetch_word/', views.fetch_word, name="fetch_word")
]
