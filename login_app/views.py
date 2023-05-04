from django.shortcuts import render
from django.views import View

class Home(View):
    
    def get(self, request):

        return render(request, 'index.html')

class Register(View):

    def get(self, request):
        return render(request, 'register.html')
        
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if len(password) < 8:
                messages = 'password must be greater than 8 characters'
                return render(request, 'register.html', {'error':messages})

            if User.objects.filter(username=username).exists():
                messages = 'username already taken'
                return render(request, 'register.html', {'error':messages})

            if User.objects.filter(email = email).exists():
                messages = 'email already used'
                return render(request, 'register.html', {'error':messages})
                
            user = User.objects.create_user(first_name = firstName, last_name = lastName, username=username, email=email, password=password)
            user.save()
            return redirect('login?next=/')
                
        else:
            messages = 'Password mismatch'
            return render(request, 'register.html', {'error':messages})
