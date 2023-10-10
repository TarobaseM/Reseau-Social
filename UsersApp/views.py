from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.shortcuts import redirect

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')  # Redirigez vers la page d'accueil ou une autre page après la connexion
    else:
        form = LoginForm(request)
    return render(request, 'UsersApp/login.html', {'form': form,  'registration_form': UserCreationForm()})



def logout_view(request):
    # Use Django's logout function to log out the user
    logout(request)
    # Redirect to the home page or any other page you prefer
    return redirect('home')
