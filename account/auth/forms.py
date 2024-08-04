# -*- coding: utf-8 -*-
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import get_user_model


User = get_user_model()


class PasswordChangeForm(PasswordChangeForm):
	"""Password change form class"""
	
	class Meta:
		model = User
