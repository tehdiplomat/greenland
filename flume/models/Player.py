from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

from flume.models import Game


class Player(models.Model):
	# If User is None, use AI
	user = models.ForeignKey(User, blank=True, null=True, default=None)
	name = models.CharField(max_length=50, unique=True)

	raw = models.IntegerField(default=0)
	tech = models.IntegerField(default=0)
	fuel = models.IntegerField(default=0)
	workforce = models.IntegerField(default=0)
	mineral = models.IntegerField(default=0)
	liquid = models.IntegerField(default=0)




	def __unicode__(self):
		return self.name

	class Meta:
		app_label = 'flume'
		ordering = ['name']

class CardAdmin(admin.ModelAdmin):
	list_display = ()
	ordering = ()