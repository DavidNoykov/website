from .forms import MovieForm
from .forms import MovieSearchForm
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login
from .forms import UserLoginForm
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Movie, UserProfile


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})


def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movie_detail.html', {'movie': movie})


def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')  # Redirect to movie list after adding movie
    else:
        form = MovieForm()
    return render(request, 'add_movie.html', {'form': form})


def movie_list(request):
    form = MovieSearchForm(request.GET)
    movies = Movie.objects.all()

    # Handle search query
    query = request.GET.get('query')
    if query:
        movies = movies.filter(title__icontains=query)

    # Handle search by release date
    release_date = request.GET.get('release_date')
    if release_date:
        movies = movies.filter(release_date=release_date)

    # Handle search by genre
    genre = request.GET.get('genre')
    if genre:
        movies = movies.filter(genre__icontains=genre)

    # Handle search by director
    director = request.GET.get('director')
    if director:
        movies = movies.filter(director__icontains=director)

    return render(request, 'movie_list.html', {'movies': movies, 'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('movie_list')  # Redirect to movie list page after successful login
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('movie_list')



@login_required
def add_favorite(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    profile.favorite_movies.add(movie)
    return redirect('movie_list')

@login_required
def favorite_list(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    favorite_movies = profile.favorite_movies.all()
    return render(request, 'favorite_list.html', {'favorite_movies': favorite_movies})








