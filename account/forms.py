# -*- coding: utf-8 -*-
from django import forms
from account.models import Messages


class MessageForm(forms.ModelForm):
	"""Message form class"""
	
	class Meta:
		model = Messages
		fields = ['full_name', 'email', 'text_body']
