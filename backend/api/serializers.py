from rest_framework import serializers
from .models import Pitch, PlayerPitchTypes, PlayerPitchStats, PlayerStats, PlayerBio, PlayerScouting, PlayerProfile, PlayerAdvancedStats, PlayerPitchingAttributes, PlayerHittingAttributes, PlayerRunningAttributes, PlayerFieldingAttributes, TeamProfile, Team, TeamScouting, Tutorial, UserAdvancedStats, UserStats, AtBat, Game, Coach


class PlayerRunningAttributes(serializers.ModelSerializer):
    class Meta:
        model = PlayerRunningAttributes
        fields = '__all__'

class PlayerBio(serializers.ModelSerializer):
    class Meta:
        model = PlayerBio
        fields = '__all__'

class PlayerHittingAttributes(serializers.ModelSerializer):
    class Meta:
        model = PlayerHittingAttributes
        fields = '__all__'

class PlayerFieldingAttributes(serializers.ModelSerializer):
    class Meta:
        model = PlayerFieldingAttributes
        fields = '__all__'

class PlayerRunningAttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerRunningAttributes
        fields = '__all__'

class PlayerPitchingAttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerPitchingAttributes
        fields = '__all__'

class PlayerPitchStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerPitchStats
        fields = '__all__'

class PlayerPitchTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerPitchTypes
        fields = '__all__'

class Game(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class AtBat(serializers.ModelSerializer):
    class Meta:
        model = AtBat
        fields = '__all__'

class Pitch(serializers.ModelSerializer):
    class Meta:
        model = Pitch
        fields = '__all__'

class PlayerStats(serializers.ModelSerializer):
    class Meta:
        model = PlayerStats
        fields = '__all__'

class PlayerAdvancedStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerAdvancedStats
        fields = '__all__'

class UserStats(serializers.ModelSerializer):
    class Meta:
        model = UserStats
        fields = '__all__'

class UserAdvancedStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAdvancedStats
        fields = '__all__'

class PlayerScouting(serializers.ModelSerializer):
    class Meta:
        model = PlayerScouting
        fields = '__all__'

class TeamScouting(serializers.ModelSerializer):
    class Meta:
        model = TeamScouting
        fields = '__all__'

class PlayerProfile(serializers.ModelSerializer):
    class Meta:
        model = PlayerProfile
        fields = '__all__'

class TeamProfile(serializers.ModelSerializer):
    class Meta:
        model = TeamProfile
        fields = '__all__'

class Tutorial(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = '__all__'

class Coach(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = '__all__'

class Team(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'






