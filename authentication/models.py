from django.contrib.auth.models import abstractBaseUser
from django.db import models

class Account(abstractBaseUser):
	email = models.CharField(max_length=40, unique=True)
	username = models.CharField(max_length=40, unique=True)

	first_name = models.CharField(max_length=40, blank=True)
	last_name = models.CharField(max_length=40, blank=True)
	tagline = models.CharField(max_length=40, blank=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	is_admin = models.BooleanField(default=False)

	objects = AccountManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELD = ['username']

	def __unicode__(self):
		return self.email

	def get_full_name(self):
		return ' '.join([self.first_name, self.last_name])

	def get_short_name(self):
		return self.first_name

