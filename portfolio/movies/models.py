from django.db import models


class Author(models.Model):
    name = models.CharField("Name", max_length=60, blank=True)
    last_name = models.CharField("Last name", max_length=120, blank=True)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return f"{self.pk} - {self.name} {self.last_name}"


class Movie(models.Model):
    name = models.CharField("Name", max_length=120, blank=True)
    movie_type = models.CharField("Type", max_length=30, blank=True)
    description = models.CharField("Description", max_length=300, blank=True)
    release_date = models.DateField("Release date", blank=True, null=True)

    author = models.ForeignKey(
        Author,
        verbose_name="Author",
        on_delete=models.CASCADE,
        related_name="movies",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return f"{self.pk} - {self.name}"
