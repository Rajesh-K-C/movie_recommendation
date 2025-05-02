from django.shortcuts import render, redirect
from movies.models import Movie
from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    recent_movies = Movie.objects.prefetch_related("language", "genres").order_by("-created_at")[:7]
    context = {
        "recent_movies": recent_movies
    }
    return render(request, "core/home.html", context)

from django.contrib.auth.views import LoginView
from django.shortcuts import redirect

class CustomLoginView(LoginView):
    template_name = 'core/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    
class UserRegistrationView(CreateView):
    model = User
    template_name = 'core/register.html'
    form_class = UserRegistrationForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])
        user.save()
        login(self.request, user)
        return redirect('home')