from rest_framework import viewsets

from .models import Author, Movie
from .serializers import (
    DetailAuthorSerializer,
    DetailMovieSerializer,
    ListAuthorSerializer,
    ListMovieSerializer,
)


class MovieViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.select_related("author")

    def get_serializer_class(self):
        if self.action == "retrieve":
            return DetailMovieSerializer
        return ListMovieSerializer


class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return DetailAuthorSerializer
        return ListAuthorSerializer
