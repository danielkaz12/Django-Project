from rest_framework import serializers

from movies.models import Author, Movie


class BaseMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("name", "movie_type", "description")


class ListAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("name", "last_name")


class DetailAuthorSerializer(ListAuthorSerializer):
    movies = BaseMovieSerializer(many=True)

    class Meta(ListAuthorSerializer.Meta):
        model = Author
        fields = (*ListAuthorSerializer.Meta.fields, "movies")


class DetailMovieSerializer(BaseMovieSerializer):
    author = ListAuthorSerializer(read_only=True)

    class Meta(BaseMovieSerializer.Meta):
        fields = (*BaseMovieSerializer.Meta.fields, "author")
