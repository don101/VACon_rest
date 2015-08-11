from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from VACon_rest.player import Player
from VACon_rest.serializers import PlayerSerializer
from VACon_rest.VACon import getFriendsSteamids, getPlayersBySteamids, getPlayerBySteamid

class FriendsList(APIView):
	def get(self, request, steamid, format=None):

		try:
			friendsSteamids = getFriendsSteamids(steamid)
			players = getPlayersBySteamids(friendsSteamids)
			response = PlayerSerializer(players, many=True)
			return Response(response.data)

		except Exception:
			return HttpResponse("Invalid Steam ID")



class Player(APIView):
	def get(self, request, steamid, format=None):

		try:
			
			player = getPlayerBySteamid(steamid)
			response = PlayerSerializer(player)
			return Response(response.data)
			
		except Exception:
			return HttpResponse("Invalid Steam ID")


def Default(request):
	return HttpResponse("Please use /friendslist/")