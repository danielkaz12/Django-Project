import datetime
from unittest.mock import ANY

import pytest
from django.urls import reverse
from movies.models import Author, Movie
from rest_framework import status

MOVIE_LIST = [
    {
        "author": ANY,
        "description": "Violence and redemption in a story about two "
        "hitmen working for the mafia, a gangster's wife, "
        "a boxer and a couple robbing people in a restaurant.",
        "id": ANY,
        "movie_type": "Thriller",
        "name": "Pulp Fiction",
        "release_date": "1994-10-14",
    },
    {
        "author": None,
        "description": "",
        "id": ANY,
        "movie_type": "Action",
        "name": "Avengers",
        "release_date": None,
    },
]


@pytest.fixture()
@pytest.mark.django_db()
def movies_fixture():
    author = Author.objects.create(name="Quentin", last_name="Tarantino")
    return Movie.objects.bulk_create(
        (
            Movie(
                name="Pulp Fiction",
                movie_type="Thriller",
                description=(
                    "Violence and redemption in a story about two "
                    "hitmen working for the mafia, a gangster's wife, "
                    "a boxer and a couple robbing people in a restaurant."
                ),
                release_date=datetime.date(1994, 10, 14),
                author=author,
            ),
            Movie(
                name="Avengers",
                movie_type="Action",
            ),
        ),
    )


@pytest.mark.django_db()
def test_movie_viewset_list(client, movies_fixture):
    response = client.get(reverse("movie-list"))
    assert (response.status_code, response.json()) == (status.HTTP_200_OK, MOVIE_LIST)


@pytest.mark.django_db()
def test_movie_viewset_detail(client, movies_fixture):
    response = client.get(reverse("movie-detail", kwargs={"pk": movies_fixture[0].id}))
    assert (response.status_code, response.json()) == (
        status.HTTP_200_OK,
        MOVIE_LIST[0]
        | {"author": {"id": ANY, "last_name": "Tarantino", "name": "Quentin"}},
    )
