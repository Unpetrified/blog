from unicodedata import name
from django.urls import path

from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.post, name='post'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register')
]
