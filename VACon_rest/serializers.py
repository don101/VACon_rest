from rest_framework import serializers
from VACon_rest.player import Player

class PlayerSerializer(serializers.Serializer):
    steamid = serializers.CharField()
    personaname = serializers.CharField()
    avatarfull = serializers.URLField()
    profileurl = serializers.URLField()
    VACBanned = serializers.BooleanField()
