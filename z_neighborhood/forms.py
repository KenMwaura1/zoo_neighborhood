from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import NeighborHood, UserProfile, Business, Post


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


class NeighborHoodForm(forms.ModelForm):
    class Meta:
        model = NeighborHood
        exclude = ('admin',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Neighborhood Name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Neighborhood Location'}),
            'population': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Population'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'police': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Police'}),
            'hood_logo': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Neighborhood Logo'}),
            'health': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Health'}),
            'education': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Education'}),

        }


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'neighbourhood')
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Bio'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Profile Picture'}),
        }


class UpdateNeighbourhoodForm(forms.ModelForm):
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


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user', 'neighbourhood')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Business Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Business Email'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Business Location'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Business Phone Number'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Business Description'}),
            'business_logo': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Business Image'}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'hood')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Post Content'}),
            'post_image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Post Image'}),
        }


