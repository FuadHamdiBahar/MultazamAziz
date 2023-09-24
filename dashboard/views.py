from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# from libraries.models import CustomUser
# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Replace 'home' with the URL name of your desired homepage
            return redirect('index')
        else:
            # Handle invalid login credentials
            return render(request, 'dashboard/index.html', {'msg': 'gagal'})
    else:
        return render(request, 'dashboard/index.html')


def signup_view(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        return redirect('login')
    return render(request, 'dashboard/signup.html')


def logout_view(request):
    logout(request)
    return redirect('login')
