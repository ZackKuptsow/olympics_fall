from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    ListAPIView,
    UpdateAPIView,
)
from django.views.decorators.csrf import csrf_exempt

from .models import Player, Team, Event, Game
from .serializers import (
    PlayerSerializer,
    TeamSerializer,
    AddPlayerSerializer,
    EventSerializer,
    PreGameSerializer,
    AddWinnerSerializer,
    PostGameSerializer,
)


class GetPlayersView(ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class CreatePlayerView(ListCreateAPIView):
    model = Player
    permission_classes = [permissions.AllowAny]
    serializer_class = PlayerSerializer

    # TODO: create a way to get one player -- ListCreate vs Create needs a get request
    def post(self, request, format=None, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            username = serializer.data.get("username")
            email = serializer.data.get("email")
            first_name = serializer.data.get("first_name")
            last_name = serializer.data.get("last_name")
            captain = serializer.data.get("captain")
            team = serializer.data.get("team")

            player = Player.objects.create(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                captain=captain,
                team=team,
            )
            player.save()

            return Response(PlayerSerializer(player).data, status=status.HTTP_200_OK)


class CreateTeamView(CreateAPIView):
    model = Team
    permission_classes = [permissions.AllowAny]
    serializer_class = TeamSerializer

    def post(self, request, format=None, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get("name")

            team = Team.objects.create(name=name)
            team.save()

            return Response(TeamSerializer(team).data, status=status.HTTP_200_OK)


class GetTeamsView(ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class AddPlayerToTeamView(UpdateAPIView):
    model = Player
    permission_classes = [permissions.AllowAny]
    serializer_class = AddPlayerSerializer

    def put(self, request, format=None, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            player = Player.objects.get(id=serializer.data.get("player"))
            team = Team.objects.get(id=serializer.data.get("team"))
            player.team = team
            player.save()

            return Response(PlayerSerializer(player).data, status=status.HTTP_200_OK)


class GetEventsView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class CreateEventView(CreateAPIView):
    model = Event
    permission_classes = [permissions.AllowAny]
    serializer_class = EventSerializer

    def post(self, request, format=None, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get("name")

            event = Event.objects.create(name=name)
            event.save()

            return Response(EventSerializer(event).data, status=status.HTTP_200_OK)


class CreateGameView(CreateAPIView):
    model = Game
    permission_classes = [permissions.AllowAny]
    serializer_class = PreGameSerializer

    def post(self, request, format=None, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            event = Event.objects.get(id=serializer.data.get("event"))
            round = serializer.data.get("round")
            first_team = Team.objects.get(id=serializer.data.get("first_team"))
            second_team = Team.objects.get(id=serializer.data.get("second_team"))
            on_deck = serializer.data.get("on_deck")
            is_playing = serializer.data.get("is_playing")

            game = Game.objects.create(
                event=event,
                round=round,
                first_team=first_team,
                second_team=second_team,
                on_deck=on_deck,
                is_playing=is_playing,
            )
            game.save()

            return Response(PreGameSerializer(game).data, status=status.HTTP_200_OK)


class GetGamesView(ListAPIView):
    queryset = Game.objects.all()
    serializer_class = PostGameSerializer


class AddWinnerView(UpdateAPIView):
    model = Game
    permission_classes = [permissions.AllowAny]
    serializer_class = AddWinnerSerializer

    def put(self, request, format=None, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            game = Game.objects.get(id=serializer.data.get("game"))
            game.winner = Team.objects.get(id=serializer.data.get("winner"))
            game.save()

            return Response(PostGameSerializer(game).data, status=status.HTTP_200_OK)
