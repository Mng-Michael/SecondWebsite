from django.contrib import admin

from .models import GameMode, Match, PlayerElo

# Register your models here.


class GameModeAdmin(admin.ModelAdmin):
    list_display = ('name', 'game', 'players_per_alliance',)
    list_filter = ('name', 'game', 'players_per_alliance',)
    search_fields = ('name')


class MatchAdmin(admin.ModelAdmin):
    list_display = ('match_number', 'time', 'game_mode',
                    'red_alliance', 'blue_alliance', 'red_score', 'blue_score')
    list_filter = ('match_number', 'time', 'game_mode')
    search_fields = ('match_number', 'time')


class PlayerEloAdmin(admin.ModelAdmin):
    list_display = ('player', 'game_mode', 'elo',
                    'matches_played', 'matches_won', 'matches_lost', 'matches_drawn')
    list_filter = ('game_mode')
    search_fields = ('player')


admin.site.site_header = "Second Robotics Admin Panel"
admin.site.register(GameMode, GameModeAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(PlayerElo, PlayerEloAdmin)
