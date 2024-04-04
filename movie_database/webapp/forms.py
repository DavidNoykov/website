from .models import Movie
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'release_date', 'director', 'genre', 'rating']


class MovieSearchForm(forms.Form):
    query = forms.CharField(label='Search')


class MovieSearchForm(forms.Form):
    query = forms.CharField(label='Search', required=False)
    release_date = forms.DateField(label='Release Date', required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    genre = forms.CharField(label='Genre', required=False)
    director = forms.CharField(label='Director', required=False)


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']



