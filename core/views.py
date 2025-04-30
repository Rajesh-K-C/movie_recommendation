from django.shortcuts import render
from movies.models import Movie

def home(request):
    recent_movies = Movie.objects.prefetch_related("language", "genres").order_by("-created_at")
    context = {}
    return render(request, "core/home.html", context)