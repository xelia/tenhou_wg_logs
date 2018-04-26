# -*- coding: utf-8 -*-
from django.db import models


class TenhouWgGame(models.Model):
    active = models.BooleanField(db_index=True, default=True)
    game_id = models.CharField(max_length=64, db_index=True)
    game_type = models.IntegerField()
    start_time = models.CharField(max_length=8)
    creation_datetime = models.DateTimeField(auto_now_add=True)

    @property
    def game_link(self):
        return 'http://tenhou.net/0/?wg={}'.format(self.game_id)


class TenhouWgPlayer(models.Model):
    name = models.CharField(max_length=64, db_index=True)
    dan = models.IntegerField()
    rate = models.FloatField()
    game = models.ForeignKey(TenhouWgGame, related_name='players')
