from django.urls import path
from . import views

urlpatterns = [
    path("watch/<int:pk>/", views.WatchView.as_view(), name="watch"),
]