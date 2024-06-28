from django.db import models
from django.forms import CharField


class Team(models.Model):
    # Team model
    name = models.CharField(max_length=100)

    def __str__(self) -> CharField:
        return self.name


class Person(models.Model):
    # Person model
    team = models.ForeignKey(
        Team,
        related_name='people',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"
