# -*- coding: utf-8 -*-
from django.contrib import admin

from wg_logs import models


class PlayerInline(admin.TabularInline):
    model = models.TenhouWgPlayer
    # readonly_fields = ('name', 'dan', 'rate')
    extra = 0
    can_delete = False


@admin.register(models.TenhouWgGame)
class GameAdmin(admin.ModelAdmin):
    list_display = ('game_id', 'game_type', 'start_time', 'active', 'creation_datetime')
    inlines = (PlayerInline, )

