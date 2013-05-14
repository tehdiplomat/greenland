from django.db import models
from django.contrib import admin
#from django.contrib.auth.models import User

class Card(models.Model):
	name = models.CharField(max_length=50, unique=True)
	

	def __unicode__(self):
		return self.name

	class Meta:
		app_label = 'flume'
		ordering = ['name']

class CardAdmin(admin.ModelAdmin):
	list_display = ()
	ordering = ()