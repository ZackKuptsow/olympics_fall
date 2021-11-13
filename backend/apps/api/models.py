from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Team(models.Model):
    name = models.CharField(max_length=128, default="")

    def __str__(self):
        return str(self.name)


class Player(models.Model):
    username = models.CharField(max_length=24, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=48)
    captain = models.BooleanField(default=False)
    team = models.ForeignKey(
        Team, related_name="player", null=True, blank=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return "[{}] - {} {}".format(
            self.team, self.username, "ⓒ" if self.captain else ""
        )


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
    first_team = models.ForeignKey(Team, related_name="team1", on_delete=models.PROTECT)
    second_team = models.ForeignKey(
        Team, related_name="team2", on_delete=models.PROTECT
    )
    on_deck = models.BooleanField(default=True)
    is_playing = models.BooleanField(default=False)
    winner = models.ForeignKey(
        Team,
        related_name="games_won",
        null=True,
        blank=True,
        default=None,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "{}\nRound {}\n{} vs. {}".format(
            self.event.name, self.round, self.first_team, self.second_team
        )

    def get_teams(self):
        return (self.first_team, self.second_team)

    def get_winner(self):
        return self.winner
