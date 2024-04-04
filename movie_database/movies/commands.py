from .models import Movie

def movlst():
    movies = Movie.objects.all()
    for movie in movies:
        print(f"{movie.title} - {movie.description}")

def movdt(movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
        print(f"Title: {movie.title}")
        print(f"Description: {movie.description}")
        print(f"Release Date: {movie.release_date}")
        print(f"Director: {movie.director}")
        print(f"Genre: {movie.genre}")
        print(f"Rating: {movie.rating}")
    except Movie.DoesNotExist:
        print("Movie not found.")

# Implement other commands similarly...
