from django.contrib import admin

from .models import Author, Movie


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "last_name")


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("name", "movie_type", "description", "release_date", "author")
