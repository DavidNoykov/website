from django.urls import path
from .views import movie_list, movie_detail, add_movie,register,user_login,user_logout,add_favorite,favorite_list

urlpatterns = [
    path('add_favorite/<int:movie_id>/', add_favorite, name='add_favorite'),
    path('favorites/', favorite_list, name='favorite_list'),
    path('', movie_list, name='movie_list'),
    path('movie/<int:movie_id>/', movie_detail, name='movie_detail'),
    path('add_movie/', add_movie, name='add_movie'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout')
]

