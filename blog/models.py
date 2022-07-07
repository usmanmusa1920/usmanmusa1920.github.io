from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
	"""Category table"""

	pub_date = models.DateTimeField(default=timezone.now)
	last_modified = models.DateTimeField(auto_now=True)
	publisher = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=300, blank=False, null=False)
	description = models.TextField(blank=True, null=True)
	image_url = models. CharField(max_length=1000000, blank=True, null=True)
	snippet = models.TextField(blank=True, null=True)
	url_list = models.TextField(blank=True, null=True)
	
	def __str__(self):
	  return f'{self.title}'
	

class Post(models.Model):
	"""Post table"""

	pub_date = models.DateTimeField(default=timezone.now)
	last_modified = models.DateTimeField(auto_now=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	title = models.CharField(max_length=300, blank=False, null=False)
	summary = models.TextField(blank=True, null=True)
	image_url = models. CharField(max_length=1000000, blank=True, null=True)
	snippet = models.TextField(blank=True, null=True)
	url_list = models.TextField(blank=True, null=True)
	
	def __str__(self):
		return f'{self.title}'
	

class Comment(models.Model):
	"""Comment table"""

	timestamp = models.DateTimeField(default=timezone.now)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	full_name = models.CharField(max_length=255, blank=False, null=False)
	email = models.CharField(max_length=255, blank=False, null=False)
	text_body = models.TextField(blank=False, null=False)
	is_read = models.BooleanField(default=False)
	
	def __str__(self):
		return f'{self.text_body}'
	

class Reply(models.Model):
	"""Reply table"""

	timestamp = models.DateTimeField(default=timezone.now)
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
	full_name = models.CharField(max_length=255, blank=False, null=False)
	email = models.CharField(max_length=255, blank=False, null=False)
	text_body = models.TextField(blank=False, null=False)
	is_read = models.BooleanField(default=False)
	
	def __str__(self):
		return f'{self.text_body}'
