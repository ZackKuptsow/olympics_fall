from django.urls import path
from .views import CreateTeam

app_name = "base"
urlpatterns = [
    path("create/team/", CreateTeam.as_view(), name="create_team"),
]
