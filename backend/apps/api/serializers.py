from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Player, Team, Event, Game


class PlayerSerializer(serializers.ModelSerializer):
    # def create(self, validated_data):
    #     print("#" * 10000)

    #     player = Player.objects.create_user(
    #         username=validated_data["username"],
    #         email=validated_data["email"],
    #         first_name=validated_data["first_name"],
    #         last_name=validated_data["last_name"],
    #         captain=validated_data["captain"],
    #         team=validated_data["team"],
    #     )

    #     print(player)

    #     player.save()

    #     return player

    class Meta:
        model = Player
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "captain",
            "team",
        )


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ("id", "name")


class AddPlayerSerializer(serializers.ModelSerializer):
    player = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all())
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())

    class Meta:
        model = Player
        fields = ("player", "team")


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("id", "name")


class PreGameSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())
    first_team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    second_team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())

    class Meta:
        model = Game
        fields = (
            "id",
            "event",
            "round",
            "first_team",
            "second_team",
            "on_deck",
            "is_playing",
        )


class AddWinnerSerializer(serializers.ModelSerializer):
    game = serializers.PrimaryKeyRelatedField(queryset=Game.objects.all())
    winner = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())

    class Meta:
        model = Game
        fields = ("game", "winner")


class PostGameSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())
    first_team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    second_team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    winner = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())

    class Meta:
        model = Game
        fields = (
            "id",
            "event",
            "round",
            "first_team",
            "second_team",
            "on_deck",
            "is_playing",
            "winner",
        )
