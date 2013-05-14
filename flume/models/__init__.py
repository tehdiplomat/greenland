from django.contrib import admin

from flume.models.Card import Card, CardAdmin


admin.site.register(Card, CardAdmin)