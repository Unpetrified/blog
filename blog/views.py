from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {"posts": posts})

def post(request):
    return render(request, 'post.html')

def login(request):
    return render(request, 'login.html')
    
def register(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        userName = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            
            if len(password) < 8:
                message = messages.info(request, 'password must be greater than 8 characters!')
                return redirect('register')

            if User.objects.filter(email= email).exists():
                message = messages.info(request, "email already exists")
                return redirect('register')
            
            if User.objects.filter(username= userName).exists():
                message = messages.info(request, "username is taken")
                return redirect('register')
            
            user = User.objects.create_user(first_name=firstName, last_name = lastName,username=userName, email=email, password=password)
            user.save()
            return redirect('login')

        else:
            message = messages.info(request, "passwords do not match")
            return redirect('register')

    return render(request, 'register.html')

