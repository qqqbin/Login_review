from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from .models import Profile
from django.contrib.auth.models import User 

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if request.POST['password1'] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password1"])
            nickname = request.POST["nickname"]
            email = request.POST["email"]
            phonenum = request.POST["phonenum"]
            profile = Profile(user=user, nickname=nickname, email=email, phonenum=phonenum)
            profile.save()
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'signup.html', {'form':form})
    else :
        form = UserCreationForm()
        return render(request, 'signup.html', {'form':form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect(request, 'login.html', {'form':form})
        else:
            return render(request, 'login.html', {'form':form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})

def logout(request):
    auth.logout(request)
    return redirect('main') 