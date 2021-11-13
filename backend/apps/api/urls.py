from django.urls import re_path


from .views import (
    CreatePlayerView,
    GetEventsView,
    GetPlayersView,
    CreateTeamView,
    GetTeamsView,
    AddPlayerToTeamView,
    CreateEventView,
    CreateGameView,
    GetGamesView,
    AddWinnerView,
)

app_name = "api"
urlpatterns = [
    re_path(r"^create/player/$", CreatePlayerView.as_view(), name="create_player"),
    re_path(r"^get/players/$", GetPlayersView.as_view(), name="get_players"),
    re_path(r"^create/team/$", CreateTeamView.as_view(), name="create_team"),
    re_path(r"^get/teams/$", GetTeamsView.as_view(), name="get_teams"),
    re_path(r"^add/player/$", AddPlayerToTeamView.as_view(), name="add_player"),
    re_path(r"^get/events/$", GetEventsView.as_view(), name="get_events"),
    re_path(r"^create/event/$", CreateEventView.as_view(), name="create_event"),
    re_path(r"^create/game/$", CreateGameView.as_view(), name="create_game"),
    re_path(r"^get/games/$", GetGamesView.as_view(), name="get_games"),
    re_path(r"^add/winner/$", AddWinnerView.as_view(), name="add_winner"),
]
