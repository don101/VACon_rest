class Player():
	def __init__(self, playerSummary):
		self.steamid = playerSummary['steamid']		
		self.personaname = playerSummary['personaname']
		self.avatarfull = playerSummary['avatarfull']	
		self.profileurl = playerSummary['profileurl']
		self.VACBanned = False
