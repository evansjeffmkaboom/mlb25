from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='team_logos/', blank=True, null=True)
    # Additional attributes like league/division, etc.

    def __str__(self):
        return f"{self.city} {self.name}"


class PlayerBio(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    height = models.CharField(max_length=10)
    weight = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    position = models.CharField(max_length=20)
    batting_hand = models.CharField(max_length=1, choices=[('L','Left'),('R','Right'),('S','Switch')])
    throwing_hand = models.CharField(max_length=1, choices=[('L','Left'),('R','Right')])
    headshot = models.ImageField(upload_to='player_headshots/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class PlayerHittingAttributes(models.Model):
    player = models.OneToOneField(PlayerBio, on_delete=models.CASCADE)
    contact_left = models.IntegerField()
    contact_right = models.IntegerField()
    power_left = models.IntegerField()
    power_right = models.IntegerField()
    plate_vision = models.IntegerField()
    plate_discipline = models.IntegerField()
    batting_clutch = models.IntegerField()


    def __str__(self):
        return f"Hitting Attributes for {self.player}"


class PlayerFieldingAttributes(models.Model):
    player = models.OneToOneField(PlayerBio, on_delete=models.CASCADE)
    fielding = models.IntegerField()
    arm_strength = models.IntegerField()
    arm_accuracy = models.IntegerField()
    reaction = models.IntegerField()
    blocking = models.IntegerField()

    def __str__(self):
        return f"Fielding Attributes for {self.player}"


class PlayerRunningAttributes(models.Model):
    player = models.OneToOneField(PlayerBio, on_delete=models.CASCADE)
    speed = models.IntegerField()
    stealing = models.IntegerField()
    baserunning_aggressiveness = models.IntegerField()

    def __str__(self):
        return f"Running Attributes for {self.player}"


class PlayerPitchingAttributes(models.Model):
    player = models.OneToOneField(PlayerBio, on_delete=models.CASCADE)
    stamina = models.IntegerField()
    hits_per_9 = models.IntegerField()
    k_per_9 = models.IntegerField()
    bb_per_9 = models.IntegerField()
    hr_per_9 = models.IntegerField()
    pitching_clutch = models.IntegerField()
    control = models.IntegerField()
    velocity = models.IntegerField()
    break_attr = models.IntegerField()

    def __str__(self):
        return f"Pitching Attributes for {self.player}"


class PlayerPitchTypes(models.Model):
    player = models.ForeignKey(PlayerBio, on_delete=models.CASCADE)
    pitch_name = models.CharField(max_length=50)
    velocity = models.IntegerField()
    control = models.IntegerField()
    break_attr = models.IntegerField()

    def __str__(self):
        return f"{self.pitch_name} for {self.player}"


class PlayerPitchStats(models.Model):
    player = models.ForeignKey(PlayerBio, on_delete=models.CASCADE)
    pitch = models.ForeignKey(PlayerPitchTypes, on_delete=models.CASCADE)
    usage_rate = models.FloatField()
    effectiveness_rating = models.FloatField()

    def __str__(self):
        return f"Pitch Stats for {self.player} - {self.pitch}"


class Game(models.Model):
    home_team = models.ForeignKey(Team, related_name='home_games', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_games', on_delete=models.CASCADE)
    date = models.DateField()
    venue = models.CharField(max_length=200)
    home_score = models.IntegerField(default=0)
    away_score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.away_team} @ {self.home_team} on {self.date}"


class AtBat(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    batter = models.ForeignKey(PlayerBio, on_delete=models.CASCADE, related_name='batter_atbats')
    pitcher = models.ForeignKey(PlayerBio, on_delete=models.CASCADE, related_name='pitcher_atbats')
    inning = models.IntegerField()
    result = models.CharField(max_length=50)

    def __str__(self):
        return f"At Bat in {self.game} - Inning {self.inning}"


class Pitch(models.Model):
    at_bat = models.ForeignKey(AtBat, on_delete=models.CASCADE)
    pitch_type = models.ForeignKey(PlayerPitchTypes, on_delete=models.CASCADE)
    velocity = models.IntegerField()
    location_x = models.FloatField()
    location_y = models.FloatField()
    outcome = models.CharField(max_length=50)

    def __str__(self):
        return f"Pitch in {self.at_bat}"


class PlayerStats(models.Model):
    player = models.ForeignKey(PlayerBio, on_delete=models.CASCADE)
    games_played = models.IntegerField(default=0)
    at_bats = models.IntegerField(default=0)
    hits = models.IntegerField(default=0)
    doubles = models.IntegerField(default=0)
    triples = models.IntegerField(default=0)
    home_runs = models.IntegerField(default=0)
    rbi = models.IntegerField(default=0)
    walks = models.IntegerField(default=0)
    strikeouts = models.IntegerField(default=0)
    stolen_bases = models.IntegerField(default=0)
    caught_stealing = models.IntegerField(default=0)

    def __str__(self):
        return f"Stats for {self.player}"


class PlayerAdvancedStats(models.Model):
    player = models.ForeignKey(PlayerBio, on_delete=models.CASCADE)
    wOBA = models.FloatField()
    wRC_plus = models.FloatField()
    xBA = models.FloatField()
    xSLG = models.FloatField()
    xWOBA = models.FloatField()
    fWAR = models.FloatField()

    def __str__(self):
        return f"Advanced Stats for {self.player}"


class UserStats(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # Track user interactions, game predictions, etc.
    favorite_team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    # Additional fields for user engagement

    def __str__(self):
        return f"User Stats for {self.user.username}"


class UserAdvancedStats(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # Custom user-based advanced metrics
    engagement_score = models.FloatField()

    def __str__(self):
        return f"Advanced User Stats for {self.user.username}"


class PlayerScouting(models.Model):
    player = models.ForeignKey(PlayerBio, on_delete=models.CASCADE)
    scouting_report = models.TextField()
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Scouting Report for {self.player}"


class TeamScouting(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    scouting_report = models.TextField()
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Team Scouting Report for {self.team}"


class PlayerProfile(models.Model):
    player = models.ForeignKey(PlayerBio, on_delete=models.CASCADE)
    biography = models.TextField()
    highlight_video = models.FileField(upload_to='player_videos/', blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.player}"


class TeamProfile(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    history = models.TextField()
    highlight_video = models.FileField(upload_to='team_videos/', blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.team}"


class Tutorial(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    media = models.FileField(upload_to='tutorials/', blank=True, null=True)

    def __str__(self):
        return self.title


class Coach(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    role = models.CharField(max_length=50)
    headshot = models.ImageField(upload_to='coach_headshots/', blank=True, null=True)

    def __str__(self):
        return f"Coach {self.first_name} {self.last_name}"
