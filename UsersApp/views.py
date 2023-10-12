from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm  # Importez à la fois LoginForm et RegistrationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(request, data=request.POST)  # Renommez le formulaire en "login_form"
        
        
        if login_form.is_valid():
            login(request, login_form.get_user())
            return redirect('home')  # Redirigez vers la page d'accueil ou une autre page après la connexion
    else:
        login_form = LoginForm(request)  # Renommez le formulaire en "login_form"
    registration_form = RegistrationForm(request.POST)
    return render(request, 'UsersApp/login.html', {'login_form': login_form,'registration_form': registration_form})  # Renommez le formulaire en "login_form"

def registration_view(request):
    if request.method == "POST":
     registration_form = RegistrationForm(request.POST)
     if registration_form.is_valid():
        new_user = registration_form.save()
        login(request, new_user)
        return redirect('home')  # Redirect to the home page or another appropriate page

    else:
        registration_form = RegistrationForm()
        return redirect('login')

    return render(request,  {'registration_form': registration_form})
