from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class LoginForm(AuthenticationForm):
    class Meta:
        model = User # Remplacez User par votre modèle d'utilisateur personnalisé le cas échéant
        fields = ['username', 'password']
    
    


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User # Remplacez User par votre modèle d'utilisateur personnalisé le cas échéant
        fields = ['username', 'password1', 'password2']
