from django.shortcuts import render, redirect
from movies.models import Movie
from django.contrib.auth import login
from .forms import UserRegistrationForm, ProfileUpdateForm, CustomPasswordChangeForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from datetime import timedelta
from django.utils import timezone
from django.db.models import Count, Q, F, FloatField, ExpressionWrapper
from django.contrib.auth.views import LoginView

def home(request):
    last_7_days = timezone.now() - timedelta(days=7)
    recent_movies = Movie.objects.prefetch_related("language", "genres").filter(created_at__gt=last_7_days).order_by("-created_at")[:8]
    if len(recent_movies) == 8:
        recent_movies = recent_movies[:7]
        new_more = True
    else:
        new_more = False
    popular_movies = Movie.objects.prefetch_related("genres", "language").annotate(
            recent_likes=Count("likes", filter=Q(likes__created_at__gte=last_7_days)),
            recent_views=Count("views", filter=Q(views__created_at__gte=last_7_days))
        ).annotate(
            popularity=ExpressionWrapper(
                F("recent_likes") / (F("recent_views") + 1.0),
                output_field=FloatField()
            )
        )
    popular_movies = popular_movies.filter(popularity__gt=0).order_by("-popularity", "-recent_likes", "-recent_views", "-pk")

    if len(popular_movies) == 8:
        popular_movies = popular_movies[:7]
        popular_more = True
    else:
        popular_more = False

    context = {
        "recent_movies": recent_movies,
        "new_more": new_more,
        "popular_movies": popular_movies,
        "popular_more":popular_more,
    }
    return render(request, "core/home.html", context)

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
    
class ProfileView(LoginRequiredMixin, FormView):
    template_name = "core/profile.html"
    form_class = ProfileUpdateForm
    success_url = "/profile/"

    def get_initial(self):
        return {
            'first_name': self.request.user.first_name,
            'last_name': self.request.user.last_name,
            'email': self.request.user.email,
        }

    def form_valid(self, form):
        user = self.request.user
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.email = form.cleaned_data['email']
        user.save()
        messages.success(self.request, "Profile updated successfully.")
        return super().form_valid(form)

class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = "core/change_password.html"
    form_class = CustomPasswordChangeForm
    success_url = "/change-password/"
