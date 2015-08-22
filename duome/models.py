# -*- coding: utf-8 -*-
__author__ = 'Phoenix'

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	nickname = models.CharField(max_length=64, blank=True)
	ucode = models.IntegerField(default=0)

	def __unicode__(self):
		return self.user.username
