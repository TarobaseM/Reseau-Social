from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')  # Redirigez vers la page d'accueil ou une autre page après la connexion
    else:
        form = LoginForm(request)
    return render(request, 'UsersApp/login.html', {'form': form,  'registration_form': UserCreationForm()})


