from __future__ import unicode_literals
from django.db import models
from ..login.models import Users
print Users

class BookManager(models.Manager):
	pass

class AuthorManager(models.Manager):
	pass

class Books(models.Model):
	bookName = models.CharField(max_length=50)
	bookDesc = models.TextField()
	author = models.ForeignKey('Authors',on_delete=models.CASCADE)
	added_by = models.ForeignKey('login.Users',on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = BookManager()

class Authors(models.Model):

	a_first_name = models.CharField(max_length=80)
	a_last_name = models.CharField(max_length=80)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	added_by = models.ForeignKey('login.Users',on_delete=models.CASCADE)

	objects = AuthorManager()
