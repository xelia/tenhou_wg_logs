# -*- coding: utf-8 -*-
from rest_framework import serializers

from wg_logs import models


class PlayerInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TenhouWgPlayer
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    players = PlayerInlineSerializer(many=True)
    game_link = serializers.CharField()

    class Meta:
        model = models.TenhouWgGame
        fields = '__all__'


class PlayerSerializer(PlayerInlineSerializer):
    game = GameSerializer()
