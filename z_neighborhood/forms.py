from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from z_neighborhood.models import NeighborHood


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
                             max_length=100, help_text='Required, enter a valid email address')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        }


class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = NeighborHood
        exclude = ('admin',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Neighborhood Name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Neighborhood Location'}),
            'population': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Population'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'police': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Police'}),
            'health': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Health'}),
            'education': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Education'}),
            'hood_logo': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Neighborhood Image'}),
        }


