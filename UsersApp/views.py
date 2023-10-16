from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import logout
from django.shortcuts import redirect

from social_django.models import UserSocialAuth





def google_login(request):
    if request.user.is_authenticated:
        # L'utilisateur est déjà connecté, redirigez-le vers une page appropriée
        return redirect('home')

    return render(request, 'account/login.html')

def google_logout(request):
    # Déconnecte l'utilisateur de Google
    user = request.user
    if user.is_authenticated:
        social = UserSocialAuth.objects.filter(user=user).first()
        if social:
            social.extra_data = {}
            social.save()
    return redirect('login')
