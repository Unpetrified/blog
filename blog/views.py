import re
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {"posts": posts})

def post(request, pk):
    article = Post.objects.get(id=pk)
    posts = Post.objects.all()

    data = {'article' : article, 'posts' : posts}
    return render(request, 'post.html', data)

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username= username, password= password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        
        else:
            if User.objects.filter(username= username).exists():
                messages.info(request, 'incorrect password')
            else:
                messages.info(request, 'invalid username')
            return redirect('login')

    return render(request, 'login.html')
    
def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:

            if User.objects.filter(username=username).exists():

                messages.info(request, 'username already taken')
                return redirect('register')

            if User.objects.filter(email = email).exists():

                messages.info(request, 'email already used')
                return redirect('register')
            
            user = User.objects.create_user(first_name = firstName, last_name = lastName, username=username, email=email, password=password)
            user.save()
            return redirect('login')
            
        else:
            messages.info(request, 'Password mismatch')
            return redirect('register')

    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')