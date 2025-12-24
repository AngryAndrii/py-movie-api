from django.urls import path

from cinema.views import (movies_list,
                          movie_create,
                          movie_delete,
                          movie_detail,
                          movie_update)
from core.urls import urlpatterns

app_name = "cinema"

urlpatterns = [
    path("cinema/movies/", movies_list, name="movie_list"),
    path("cinema/movies/<int:pk>", movie_detail, name="movie_detail"),
    path("cinema/movies/", movie_create, name="movie_create"),
    path("cinema/movies/<int:pk>", movie_update, name="movie_update"),
    path("cinema/movies/<int:pk>", movie_delete, name="movie_delete")
]
