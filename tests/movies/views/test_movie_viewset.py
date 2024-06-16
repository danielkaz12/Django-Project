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
def authors_fixture():
    return Author.objects.bulk_create(
        (
            Author(name="Quentin", last_name="Tarantino"),
            Author(name="David", last_name="Yates"),
        ),
    )


@pytest.fixture()
@pytest.mark.django_db()
def movies_fixture(authors_fixture):
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
                author=authors_fixture[0],
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


@pytest.mark.django_db()
def test_movie_viewset_create(client, movies_fixture, authors_fixture):
    response = client.post(
        reverse("movie-list"),
        {
            "name": "Harry Potter and the Order of Phoenix",
            "movie_type": "Fantasy",
            "description": (
                "With their warning about Lord Voldemort's return scoffed at, "
                "Harry and Dumbledore are targeted by the Wizard authorities as an "
                "authoritarian bureaucrat slowly seizes power at Hogwarts."
            ),
            "release_date": "2007-07-27",
            "author": authors_fixture[1].id,
        },
    )
    assert (response.status_code, response.json()) == (
        status.HTTP_201_CREATED,
        {
            "author": authors_fixture[1].id,
            "description": (
                "With their warning about Lord Voldemort's return scoffed at, "
                "Harry and Dumbledore are targeted by the Wizard authorities as an "
                "authoritarian bureaucrat slowly seizes power at Hogwarts."
            ),
            "id": ANY,
            "movie_type": "Fantasy",
            "name": "Harry Potter and the Order of Phoenix",
            "release_date": "2007-07-27",
        },
    )
