from django.urls import path
from . import views

urlpatterns = [
    path("watch/<int:pk>/", views.WatchView.as_view(), name="watch"),
    path("popular/", views.PopularMoviesView.as_view(), name="popular_movies"),
    path("genres/", views.MovieGenreView.as_view(), name="movie_genre_list"),
    path("genre/<int:pk>/", views.MovieByGenreView.as_view(), name="movie_list_by_genre"),
    path("new-releases/", views.NewMovieListView.as_view(), name="new_releases"),
    path("my-list/", views.MyListMovieListView.as_view(), name="my_list"),
    path("watch-history/", views.WatchHistoryMovieListView.as_view(), name="watch_history"),
    path("", views.MovieListView.as_view(), name="movies"),
    path("like/", views.LikeMovie.as_view(), name="like"),
    path("update-history/", views.UpdateHistory.as_view(), name="update_history"),
    path("add-to-my-list/", views.ToggleMyListView.as_view(), name="toggle_my_list"),
]