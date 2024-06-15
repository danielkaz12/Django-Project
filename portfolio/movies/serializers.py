from rest_framework import serializers

from .models import Author, Movie


class BaseMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("name", "movie_type", "description", "release_date")


class BaseReadMovieSerializer(BaseMovieSerializer):
    class Meta(BaseMovieSerializer.Meta):
        fields = ("id", *BaseMovieSerializer.Meta.fields)


class ListMovieSerializer(BaseReadMovieSerializer):
    class Meta(BaseReadMovieSerializer.Meta):
        fields = (*BaseReadMovieSerializer.Meta.fields, "author")


class ListAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("id","name", "last_name")


class DetailAuthorSerializer(ListAuthorSerializer):
    movies = BaseReadMovieSerializer(many=True)

    class Meta(ListAuthorSerializer.Meta):
        model = Author
        fields = (*ListAuthorSerializer.Meta.fields, "movies")


class DetailMovieSerializer(ListMovieSerializer):
    author = ListAuthorSerializer(read_only=True)
