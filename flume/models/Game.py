from django.db import models
from django.contrib import admin
from flume.models import Player

class Game(models.Model):
	name = models.CharField(max_length=50, unique=True)
	greenland = models.ForeignKey(Player)
	denmark = models.ForeignKey(Player)

	age = models.IntegerField(default=1)
	#library
	#discard

	def __unicode__(self):
		return self.name

	class Meta:
		app_label = 'flume'
		ordering = ['name']

class CardAdmin(admin.ModelAdmin):
	list_display = ()
	ordering = ()