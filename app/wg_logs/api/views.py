# -*- coding: utf-8 -*-
from rest_framework import viewsets, filters, pagination

from wg_logs.api import serializers
from wg_logs import models


class GamesViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.GameSerializer
    queryset = models.TenhouWgGame.objects.filter(active=True).order_by('creation_datetime')
    filter_backends = (filters.SearchFilter,)
    search_fields = ('players__name',)


class PlayerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.TenhouWgPlayer.objects.order_by('name', '-game__creation_datetime').distinct('name')
    serializer_class = serializers.PlayerSerializer
    lookup_field = 'name'

