from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from VACon_rest.player import Player
from VACon_rest.serializers import PlayerSerializer
from VACon_rest.VACon import getFriendsSteamids, getPlayersBySteamids

class FriendsList(APIView):
	def get(self, request, steamid, format=None):

		friendsSteamids = getFriendsSteamids(steamid)
		players = getPlayersBySteamids(friendsSteamids)

		response = PlayerSerializer(players, many=True)
		return Response(response.data)



def Default(request):
	return HttpResponse("Please use /friendslist/")