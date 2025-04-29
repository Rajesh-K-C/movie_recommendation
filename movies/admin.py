from django.contrib import admin
from .models import Movie, Genre, Language
from django.utils.html import format_html

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_movies')
    search_fields = ('name',)
    
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_poster', 'language', 'genre_list', 'total_views', 'total_likes')
    list_filter = ('language', 'genres')
    search_fields=('title', )
    exclude = ("total_views", "total_likes")
    filter_horizontal = ('genres',)
    readonly_fields = ('created_at', 'updated_at')

    def display_poster(self, obj):
        return format_html('<img src="{}" width="60" />', obj.poster.url)
    display_poster.short_description = 'Poster'
    
    def genre_list(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])
    genre_list.short_description = 'Genres'

admin.site.register(Genre, GenreAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Movie, MovieAdmin)