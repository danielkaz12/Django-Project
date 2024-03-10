# Generated by Django 5.0.2 on 2024-03-10 20:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(blank=True, max_length=60, verbose_name="Name"),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=120, verbose_name="Last name"
                    ),
                ),
            ],
            options={"verbose_name": "Author", "verbose_name_plural": "Authors",},
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(blank=True, max_length=120, verbose_name="Name"),
                ),
                (
                    "movie_type",
                    models.CharField(blank=True, max_length=30, verbose_name="Type"),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True, max_length=300, verbose_name="Description"
                    ),
                ),
                (
                    "release_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Release date"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="movies",
                        to="movies.author",
                        verbose_name="Author",
                    ),
                ),
            ],
            options={"verbose_name": "Movie", "verbose_name_plural": "Movies",},
        ),
    ]
