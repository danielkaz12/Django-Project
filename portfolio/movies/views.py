from rest_framework import viewsets

from .models import Author, Movie
from .serializers import (
    BaseMovieSerializer,
    DetailAuthorSerializer,
    DetailMovieSerializer,
    ListAuthorSerializer,
)


class MovieViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.select_related("author")

    def get_serializer_class(self):
        if self.action == "create":
            return BaseMovieSerializer
        if self.action == "retrieve":
            return DetailMovieSerializer
        return BaseMovieSerializer


class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return DetailAuthorSerializer
        return ListAuthorSerializer
