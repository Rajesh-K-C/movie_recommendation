from django.urls import path
from . import views

urlpatterns = [
    path("watch/<int:pk>/", views.WatchView.as_view(), name="watch"),
    path("popular/", views.PopularMoviesView.as_view(), name="popular_movies"),
]