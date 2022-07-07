# -*- coding: utf-8 -*-
from django import forms
from .models import (
	Post,
	Comment,
	Reply,
	Category)


class CategoryForm(forms.ModelForm):
	"""Category form class"""

	url_list_name = forms.CharField(max_length=255, required=False)
	url_list_value = forms.CharField(max_length=255, required=False)
	
	class Meta:
		model = Category
		fields = ['title', 'description', 'image_url', 'snippet', 'url_list']


class PostForm(forms.ModelForm):
	"""Post form class"""

	url_list_name = forms.CharField(max_length=255, required=False)
	url_list_value = forms.CharField(max_length=255, required=False)
	
	class Meta:
		model = Post
		fields = ['title', 'summary', 'image_url', 'snippet', 'url_list']


class CommentForm(forms.ModelForm):
	"""Comment form class"""

	class Meta:
		model = Comment
		fields = ['full_name', 'email', 'text_body']

		
class ReplyForm(forms.ModelForm):
	"""Reply form class"""

	class Meta:
		model = Reply
		fields = ['full_name', 'email', 'text_body']
