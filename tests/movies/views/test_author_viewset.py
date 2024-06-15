import datetime
from unittest.mock import ANY

import pytest
from django.urls import reverse
from movies.models import Author, Movie
from rest_framework import status

AUTHOR_LIST = [
    {"id": ANY, "last_name": "Tarantino", "name": "Quentin"},
    {"id": ANY, "last_name": "Russo", "name": "Russo"},
    {"id": ANY, "last_name": "Oldman", "name": "Gary"},
]


@pytest.fixture()
@pytest.mark.django_db()
def authors_fixture():
    authors = Author.objects.bulk_create(
        (
            Author(name="Quentin", last_name="Tarantino"),
            Author(name="Russo", last_name="Russo"),
            Author(name="Gary", last_name="Oldman"),
        ),
    )
    Movie.objects.bulk_create(
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
                author=authors[0],
            ),
            Movie(name="Avengers", movie_type="Action", author=authors[1]),
            Movie(
                name="Avengers: Infinity War",
                movie_type="Action",
                author=authors[1],
            ),
        ),
    )
    return authors


@pytest.mark.django_db()
def test_author_viewset_list(client, authors_fixture):
    response = client.get(reverse("author-list"))
    assert (response.status_code, response.json()) == (status.HTTP_200_OK, AUTHOR_LIST)


@pytest.mark.django_db()
def test_author_viewset_detail(client, authors_fixture):
    response = client.get(
        reverse("author-detail", kwargs={"pk": authors_fixture[1].id}),
    )
    assert (response.status_code, response.json()) == (
        status.HTTP_200_OK,
        AUTHOR_LIST[1]
        | {
            "movies": [
                {
                    "description": "",
                    "id": ANY,
                    "movie_type": "Action",
                    "name": "Avengers",
                    "release_date": None,
                },
                {
                    "description": "",
                    "id": ANY,
                    "movie_type": "Action",
                    "name": "Avengers: Infinity War",
                    "release_date": None,
                },
            ],
        },
    )


@pytest.mark.django_db()
def test_author_viewset_create(client):
    response = client.post(
        reverse("author-list"),
        {"last_name": "Scorsese", "name": "Martin"},
    )
    assert (response.status_code, response.json()) == (
        status.HTTP_201_CREATED,
        {
            "id": ANY,
            "last_name": "Scorsese",
            "name": "Martin",
        },
    )
