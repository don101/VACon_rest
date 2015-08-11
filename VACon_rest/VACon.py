import sys
import urllib.request
import json
from VACon_rest.player import Player

APIKey = 'YOUR API KEY HERE'


def getFriendsSteamids(steamid):
	"""Returns a List of Strings containing the 64-bit Steam IDs of the friends of the steam ID parameter"""

	friendsResponse = urllib.request.urlopen('http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=' 
		+ APIKey 
		+ '&steamid='
		+ steamid 
		+ '&relationship=friend')

	friendsJSON = friendsResponse.read().decode('utf-8')
	friends = json.loads(friendsJSON)['friendslist']['friends']
	friendsSteamids = []

	for friend in friends:
		friendsSteamids.append(friend['steamid'])

	return friendsSteamids
		

def getPlayersBySteamids(listOfSteamids):
	"""Builds and returns a List of Player objects based on the list of Steam IDs passed."""
	

	splitList=[listOfSteamids[x:x+100] for x in range(0, len(listOfSteamids), 100)]	#We split the list because the Steam Web API only processes the first 100 Steam IDs passed.
	players = []

	for sublist in splitList:
		summariesRequestString = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=' + APIKey + '&steamids='
		bansRequestString = 'http://api.steampowered.com/ISteamUser/GetPlayerBans/v1/?key=' + APIKey + '&steamids='
		for steamid in sublist:
			summariesRequestString+= steamid
			summariesRequestString+= ','

			bansRequestString+= steamid
			bansRequestString+= ','

		summariesResponse = urllib.request.urlopen(summariesRequestString)		
		summariesJSON = summariesResponse.read().decode('UTF-8')

		playerSummaries = json.loads(summariesJSON)['response']['players']
		for playerSummary in playerSummaries:
			players.append(Player(playerSummary))

		bansResponse = urllib.request.urlopen(bansRequestString)
		bansJSON = bansResponse.read().decode('UTF-8')

		playerBans = json.loads(bansJSON)['players']

		for playerBan in playerBans:
			if (playerBan['VACBanned'] == True):
				for player in players:
					if (playerBan['SteamId'] == player.steamid):
						player.VACBanned = True


	return players

def getPlayerBySteamid(steamid):
	"""Builds and returns a List of Player objects based on the list of Steam IDs passed."""

	summaryRequestString = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=' + APIKey + '&steamids=' + steamid
	bansRequestString = 'http://api.steampowered.com/ISteamUser/GetPlayerBans/v1/?key=' + APIKey + '&steamids=' + steamid


	summaryResponse = urllib.request.urlopen(summaryRequestString)		
	summaryJSON = summaryResponse.read().decode('UTF-8')

	print(summaryJSON)
	playerSummary = json.loads(summaryJSON)['response']['players'][0]	
	player = Player(playerSummary)

	bansResponse = urllib.request.urlopen(bansRequestString)
	bansJSON = bansResponse.read().decode('UTF-8')
	playerBan = json.loads(bansJSON)['players'][0]
	
	if (playerBan['VACBanned'] == True):
		player.VACBanned = True

	
	return player



