from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Team(models.Model):
    name = models.CharField(max_length=128, default="")

    def __str__(self):
        return str(self.name)


class Player(models.Model):
    user = models.OneToOneField(
        User, unique=True, related_name="player", on_delete=models.CASCADE
    )
    captain = models.BooleanField(default=False)
    team = models.ForeignKey(
        Team, related_name="player", null=True, blank=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.user)


class Event(models.Model):
    name = models.CharField(max_length=128, default="")

    def __str__(self):
        return str(self.name)


class Game(models.Model):
    event = models.ForeignKey(
        Event, related_name="game", null=True, blank=True, on_delete=models.CASCADE
    )
    round = models.IntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(6)]
    )
    first_team = models.ForeignKey(
        Team, related_name="team1", null=True, blank=True, on_delete=models.CASCADE
    )
    second_team = models.ForeignKey(
        Team, related_name="team2", null=True, blank=True, on_delete=models.CASCADE
    )
    winner = models.ForeignKey(Team, related_name="games_won", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.event.name) + "\nRound " + str(self.round)

    def get_teams(self):
        return (self.first_team, self.second_team)

    def get_winner(self):
        return self.winner
