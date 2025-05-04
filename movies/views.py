from django.shortcuts import render
from django.views import generic
from movies.models import Movie, Genre
from movie_recommendation.utils import format_minutes
from django.contrib.auth.mixins import LoginRequiredMixin

class WatchView(LoginRequiredMixin, generic.DetailView):
    model = Movie
    template_name = "movies/watch.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["movie"].duration = format_minutes(context["movie"].duration)
        context["similar_movies"] = Movie.objects.exclude(id=self.object.id)[:14]
        return context

class PopularMoviesView(LoginRequiredMixin, generic.ListView):
    model = Movie
    queryset = Movie.objects.prefetch_related("genres", "language").order_by("-pk")
    template_name = "movies/movie_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Popular Movies"
        return context

class MovieGenreView(LoginRequiredMixin, generic.ListView):
    model = Genre
    queryset = Genre.objects.all().order_by("name")
    template_name = "movies/movie_genre_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["genre_list"] = [movie for movie in context["genre_list"] if movie.total_movies > 0]
        return context

class MovieByGenreView(LoginRequiredMixin, generic.ListView):
    model = Movie
    template_name = "movies/movie_list.html"

    def get_queryset(self):
        self.genre = Genre.objects.get(pk=self.kwargs['pk'])
        return Movie.objects.filter(genres=self.genre).order_by("-pk")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"{self.genre.name} Movies"
        return context

class NewMovieListView(LoginRequiredMixin, generic.ListView):
    model = Movie
    template_name = "movies/movie_list.html"
    queryset = Movie.objects.order_by("-pk")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New Releases"
        return context