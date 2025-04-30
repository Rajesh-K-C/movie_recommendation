from django.contrib import admin
from django.urls import reverse
from .models import Movie, Genre, Language
from django.utils.html import format_html

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_movies', 'delete_button')
    search_fields = ('name',)

    def delete_button(self, obj):
        delete_url = reverse(f'admin:{obj._meta.app_label}_{obj._meta.model_name}_delete', args=[obj.pk])
        return format_html(
            '<a class="button" href="{}">Delete</a>',
            delete_url
        )
    delete_button.short_description = 'Delete'
    
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'delete_button' )
    search_fields = ('name',)
    def delete_button(self, obj):
        delete_url = reverse(f'admin:{obj._meta.app_label}_{obj._meta.model_name}_delete', args=[obj.pk])
        return format_html(
            '<a class="button" href="{}">Delete</a>',
            delete_url
        )
    delete_button.short_description = 'Delete'

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_poster', 'language', 'genre_list', 'total_views', 'total_likes', 'delete_button')
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
    
    def delete_button(self, obj):
        delete_url = reverse(f'admin:{obj._meta.app_label}_{obj._meta.model_name}_delete', args=[obj.pk])
        return format_html(
            '<a class="button" href="{}">Delete</a>',
            delete_url
        )
    delete_button.short_description = 'Delete'

admin.site.register(Genre, GenreAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Movie, MovieAdmin)