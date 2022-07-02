from django.urls import path
from blog import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:pk>', views.post, name='post'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('<str:post_id>', views.comment, name='comment'),
]
