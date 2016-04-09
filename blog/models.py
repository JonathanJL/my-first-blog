from django.db import models
from django.utils import timezone


# class is a special keyword that shows we are defining and object
# Post is the name of our model. We can give it a different name 
# but we must avoid special characters and whitespaces
# models.Model means that the Post is a Django Model, so Django knows it should be saved in the database

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	publish_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.publish_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
