from rest_framework import serializers

from mySiteApp.models import GameLevel

class GameLevelSerializer(serializers.ModelSerializer):
   class Meta:
       model = GameLevel
       fields = ('level', 'level_type')