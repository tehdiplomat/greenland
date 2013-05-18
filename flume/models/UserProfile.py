from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)

	def __unicode__(self):
		return "%s's profile" % self.user.username

	class Meta:
		app_label = 'flume'

def getProfile(user):
	try:
		return user.userprofile
	except:
		pro = UserProfile()
		pro.user = user
		pro.save()
		return user.userprofile

User.profile = property(getProfile)