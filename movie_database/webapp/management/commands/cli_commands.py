from django.core.management.base import BaseCommand
from webapp.models import Movie, UserProfile


class Command(BaseCommand):
    help = 'Custom CLI commands for managing movies'

    def add_arguments(self, parser):
        parser.add_argument('command', type=str, help='Command name (movlst, movdt, movsrch, movadd, movfv, movcat)')

    def handle(self, *args, **kwargs):
        command = kwargs['command']

        if command == 'movlst':
            self.list_movies()
        elif command == 'movdt':
            self.show_movie_details()
        elif command == 'movsrch':
            self.search_movies()
        elif command == 'movadd':
            self.add_movie()
        elif command == 'movfv':
            self.mark_favorite_movie()
        elif command == 'movcat':
            self.show_movie_categories()
        else:
            self.stderr.write("Invalid command")

    def list_movies(self):
        movies = Movie.objects.all()
        for movie in movies:
            self.stdout.write(movie.title)

    def show_movie_details(self):
        movie_id = input("Enter movie ID: ")
        try:
            movie = Movie.objects.get(id=movie_id)
            self.stdout.write(movie.title)
            self.stdout.write(movie.description)
            # Add other movie details
        except Movie.DoesNotExist:
            self.stderr.write("Movie not found")

    def search_movies(self):
        query = input("Enter search query: ")
        movies = Movie.objects.filter(title__icontains=query)
        for movie in movies:
            self.stdout.write(movie.title)

    def add_movie(self):
        title = input("Enter title: ")
        description = input("Enter description: ")
        release_date = input("Enter release date (YYYY-MM-DD): ")
        director = input("Enter director: ")
        genre = input("Enter genre: ")
        try:
            Movie.objects.create(
                title=title,
                description=description,
                release_date=release_date,
                director=director,
                genre=genre
            )
            self.stdout.write("Movie added successfully")
        except Exception as e:
            self.stderr.write("Failed to add movie: " + str(e))

    def mark_favorite_movie(self):
        movie_id = input("Enter movie ID: ")
        user_id = input("Enter user ID: ")
        try:
            movie = Movie.objects.get(id=movie_id)
            user_profile, created = UserProfile.objects.get_or_create(user_id=user_id)
            user_profile.favorite_movies.add(movie)
            self.stdout.write("Movie marked as favorite")
        except Exception as e:
            self.stderr.write("Failed to mark movie as favorite: " + str(e))

    def show_movie_categories(self):
        most_liked_movies = Movie.objects.order_by('-rating')[:5]
        newest_movies = Movie.objects.order_by('-release_date')[:5]

        self.stdout.write("Most Liked Movies:")
        for movie in most_liked_movies:
            self.stdout.write(movie.title)

        self.stdout.write("\nNewest Movies:")
        for movie in newest_movies:
            self.stdout.write(movie.title)
