# -*- coding: utf-8 -*-
from django.http import Http404
from rest_framework import viewsets, filters
from rest_framework.response import Response

from wg_logs.api import serializers
from wg_logs import models


class GamesViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.GameSerializer
    queryset = models.TenhouWgGame.objects.filter(active=True).order_by('creation_datetime')
    filter_backends = (filters.SearchFilter,)
    search_fields = ('players__name',)


class PlayerViewSet(viewsets.ViewSet):
    queryset = models.TenhouWgPlayer.objects.all()
    def retrieve(self, request, pk=None):
        player = self.queryset.filter(name=pk).order_by('-game__creation_datetime').first()
        if not player:
            raise Http404()
        serializer = serializers.PlayerSerializer(player)
        return Response(serializer.data)