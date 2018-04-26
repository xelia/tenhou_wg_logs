# -*- coding: utf-8 -*-
import json
import re
from base64 import b64decode

import requests
from django.core.management import BaseCommand
from django.conf import settings

from wg_logs import models


class Command(BaseCommand):
    def handle(self, *args, **options):
        text = requests.get(settings.TENHOU_WG_URL).text
        text = text.replace('\r\n', '')
        data = json.loads(re.match('sw\((.*)\);', text).group(1))
        active_games = []
        for game in data:
            game_id, _, start_time, game_type, *players_data = game.split(',')
            active_games.append(game_id)
            players = []
            for name, dan, rate in [players_data[i:i+3] for i in range(0, len(players_data), 3)]:
                players.append({'name': b64decode(name), 'dan': int(dan) - 9, 'rate': float(rate)})
            db_game, created = models.TenhouWgGame.objects.get_or_create(
                start_time=start_time,
                game_id=game_id,
                game_type=game_type
            )
            if created:
                for player in players:
                    models.TenhouWgPlayer.objects.create(
                        name=player['name'],
                        dan=player['dan'],
                        rate=player['rate'],
                        game=db_game
                    )
                db_game.active = True
                db_game.save()
        models.TenhouWgGame.objects.exclude(game_id__in=active_games).update(active=False)





