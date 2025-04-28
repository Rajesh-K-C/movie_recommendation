from django.db import models
from django.contrib.auth.models import User

class Language(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'languages'
        verbose_name_plural = 'languages'
        
    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=20, unique=True)
    
    class Meta:
        db_table = 'genres'
        verbose_name_plural = 'genres'

    def __str__(self):
        return self.name
    
    @property
    def total_movies(self):
        return self.movies.count()
    
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    total_views = models.PositiveIntegerField(default=0)
    total_likes = models.PositiveIntegerField(default=0)
    url = models.URLField(unique=True)
    poster = models.ImageField(upload_to='posters/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    genres = models.ManyToManyField(Genre, related_name='movies')
    language = models.ForeignKey(Language, related_name='movies', on_delete=models.CASCADE)

    class Meta:
        db_table = 'movies'
        verbose_name_plural = 'movies'

    def __str__(self):
        return self.title

class WatchHistory(models.Model):
    user = models.ForeignKey(User, related_name="watch_history", on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='watch_history', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'watch_histories'
        verbose_name_plural = 'watch_histories'

    def __str__(self):
        return f"{self.user} watched {self.movie} at {self.created_at}"
 
class View(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="views", null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="views")
    user_ip = models.IPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "views"
        verbose_name_plural = "views"
        indexes = [
            models.Index(fields=["movie", "created_at"]),
        ]

    def __str__(self):
        return f"{self.user} watched {self.movie} from {self.user_ip}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='likes', null=True) 
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "likes"
        verbose_name_plural = "likes"
        unique_together = ("user","movie")
        indexes = [
            models.Index(fields=["movie", "created_at"])
        ]

    def __str__(self):
        return f"{self.user} liked {self.movie} at {self.created_at}"

class MyList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_lists")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="my_lists")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "my_lists"
        verbose_name_plural = "my_lists"

    def __str__(self):
        return f"{self.user} added {self.movie} at {self.created_at}"