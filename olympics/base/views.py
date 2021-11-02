from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Team, Player, Event, Game


class CreateTeam(APIView):
    def post(self, request, format=None, *args, **kwargs):
        """
        Create Team object

        Args:
            request (json): json object including team name
        """
        if request.method == "POST":
            print(request)

        return Response(status=status.HTTP_200_OK)
