from django.urls import path
from . import views

urlpatterns = [
    path("watch/<int:pk>/", views.WatchView.as_view(), name="watch"),
    path("popular/", views.PopularMoviesView.as_view(), name="popular_movies"),
    path("genres/", views.MovieGenreView.as_view(), name="movie_genre_list"),
    path("genre/<int:pk>/", views.MovieByGenreView.as_view(), name="movie_list_by_genre"),
    path("new-releases/", views.NewMovieListView.as_view(), name="new-releases"),
]