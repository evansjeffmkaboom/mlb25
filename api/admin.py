from django.contrib import admin
from .models import (
    Team, PlayerBio, PlayerHittingAttributes, PlayerFieldingAttributes,
    PlayerRunningAttributes, PlayerPitchingAttributes, PlayerPitchTypes, PlayerPitchStats,
    Game, AtBat, Pitch, PlayerStats, PlayerAdvancedStats, UserStats, UserAdvancedStats,
    PlayerScouting, TeamScouting, PlayerProfile, TeamProfile, Tutorial, Coach
)

admin.site.register(Team)
admin.site.register(PlayerBio)
admin.site.register(PlayerHittingAttributes)
admin.site.register(PlayerFieldingAttributes)
admin.site.register(PlayerRunningAttributes)
admin.site.register(PlayerPitchingAttributes)
admin.site.register(PlayerPitchTypes)
admin.site.register(PlayerPitchStats)
admin.site.register(Game)
admin.site.register(AtBat)
admin.site.register(Pitch)
admin.site.register(PlayerStats)
admin.site.register(PlayerAdvancedStats)
admin.site.register(UserStats)
admin.site.register(UserAdvancedStats)
admin.site.register(PlayerScouting)
admin.site.register(TeamScouting)
admin.site.register(PlayerProfile)
admin.site.register(TeamProfile)
admin.site.register(Tutorial)
admin.site.register(Coach)
