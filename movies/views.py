from django.shortcuts import render
from django.views import generic
from movies.models import Movie
from movie_recommendation.utils import format_minutes

class WatchView(generic.DetailView):
    model = Movie
    template_name = "movies/watch.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["movie"].duration = format_minutes(context["movie"].duration)
        context["similar_movies"] = Movie.objects.exclude(id=self.object.id)[:14]
        return context
