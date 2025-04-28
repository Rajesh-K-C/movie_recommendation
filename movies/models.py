from django.db import models

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