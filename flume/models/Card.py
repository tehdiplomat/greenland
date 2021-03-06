from django.db import models
from django.contrib import admin
#from django.contrib.auth.models import User


class Card(models.Model):
	name = models.CharField(max_length=50, unique=True)
	generates = models.IntegerField(default=0) # 1 - Raw, 2 - Tech, 4 - Fuel, 8 - Workforce, 16 - Mineral, 32 -  Liquid
	# ability

	def __unicode__(self):
		return self.name

	class Meta:
		app_label = 'flume'
		ordering = ['name']

class CardAdmin(admin.ModelAdmin):
	list_display = ()
	ordering = ()