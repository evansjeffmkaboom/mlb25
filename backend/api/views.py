from django.db.models import QuerySet
from rest_framework import viewsets
from .models import *
from serializers import PlayerBio, PlayerHittingAttributes, PlayerFieldingAttributes, PlayerRunningAttributes, PlayerPitchingAttributes, PlayerStats, PlayerScouting, PlayerProfile, PlayerAdvancedStats, PlayerPitchStats, PlayerPitchingAttributesSerializer, PlayerPitchStatsSerializer, PlayerRunningAttributesSerializer, PlayerAdvancedStatsSerializer, PlayerPitchTypesSerializer, TeamScouting, Team, TeamProfile, Tutorial, UserAdvancedStatsSerializer, UserStats, Pitch, UserAdvancedStats, AtBat, Game, Coach


class PlayerBioViewSet(viewsets.ModelViewSet):
    queryset: QuerySet = PlayerBio.objects.all()
    serializers_class = PlayerBio

class PlayerHittingAttributes(viewsets.ModelViewSet):
    queryset = PlayerHittingAttributes.objects.all()
    serializers_class = PlayerHittingAttributes

class PlayerFieldingAttributes(viewsets.ModelViewSet):
    queryset = PlayerFieldingAttributes.objects.all()
    serializer_class = PlayerFieldingAttributes

class PlayerRunningAttributes(viewsets.ModelViewSet):
    queryset = PlayerRunningAttributes.objects.all()
    serializer_class = PlayerRunningAttributes

class PlayerPitchingAttributes(viewsets.ModelViewSet):
    queryset = PlayerPitchingAttributes.objects.all()
    serializer_class = PlayerPitchingAttributes

class PlayerStats(viewsets.ModelViewSet):
    queryset = PlayerStats.objects.all()
    serializer_class = PlayerStats

class PlayerScouting(viewsets.ModelViewSet):
    queryset = PlayerScouting.objects.all()
    serializer_class = PlayerScouting

class PlayerProfile(viewsets.ModelViewSet):
    queryset = PlayerProfile.objects.all()
    serializer_class = PlayerProfile

class PlayerAdvanedStats(viewsets.ModelViewSet):
    queryset = PlayerAdvancedStats.objects.all()
    serializer_class = PlayerAdvancedStats

class PlayerPitchStats(viewsets.ModelViewSet):
    queryset = PlayerPitchStatsSerializer()
    serializer_class = PlayerPitchStatsSerializer

class PlayerPitchTypes(viewsets.ModelViewSet):
    queryset = PlayerPitchTypesSerializer()
    serializer_class = PlayerPitchTypesSerializer

class PlayerPitchingAttributes(viewsets.ModelViewSet):
    queryset = PlayerPitchingAttributesSerializer()
    serializer_class = PlayerPitchingAttributesSerializer

class PlayerRunningStats(viewsets.ModelViewSet):
    queryset = PlayerRunningAttributesSerializer()
    serializer_class = PlayerRunningAttributesSerializer

class PlayerAdvancedStatsSerializer(viewsets.ModelViewSet):
    queryset = PlayerAdvancedStatsSerializer()
    serializer_class = PlayerAdvancedStatsSerializer

class TeamScouting(viewsets.ModelViewSet):
    queryset = TeamScouting()
    serializer_class = TeamScouting

class TeamProfile(viewsets.ModelViewSet):
    queryset = TeamProfile()
    serializer_class = TeamProfile
class Team(viewsets.ModelViewSet):
    queryset = Team()
    serializer_class = Team

class TeamProfile(viewsets.ModelViewSet):
    queryset = TeamProfile()
    serializer_class = TeamProfile

class Tutorial(viewsets.ModelViewSet):
    queryset = Tutorial()
    serializer_class = Tutorial

class UserAdvancedStats(viewsets.ModelViewSet):
    queryset = UserAdvancedStatsSerializer()
    serializer_class = UserAdvancedStatsSerializer

class AtBat(viewsets.ModelViewSet):
    queryset = AtBat()
    serializer_class = AtBat

class Coach(viewsets.ModelViewSet):
    queryset = Coach()
    serializer_class = Coach

class Game(viewsets.ModelViewSet):
    queryset = Game()
    serializer_class = Game

class Pitch(viewsets.ModelViewSet):
    queryset = Pitch()
    serializer_class = Pitch

class UserStats(viewsets.ModelViewSet):
    queryset = UserStats()
    serializer_class = UserStats






