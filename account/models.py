from django.db import models
from django.contrib.auth.models import (
	AbstractBaseUser,
	BaseUserManager)
from django.utils import timezone
from django.conf import settings


User = settings.AUTH_USER_MODEL


class UserAccountManager(BaseUserManager):
	"""Custom user account manager"""

	def create_user(self, first_name, last_name, username, email, password=None, **kwargs):
		"""The `**kwargs` is included to accept other keyword argument, even though it is not in this way in the django default create_user method of user class
		"""

		if not first_name:
			raise ValueError('Your first name is required')
		if not last_name:
			raise ValueError('Your last name is required')
		if not username:
			raise ValueError('Your username is required')
		if not email:
			raise ValueError('You must provide your email address')
		if not password:
			raise ValueError('You must include password')
		
		user = self.model(
			first_name = first_name,
			last_name = last_name,
			username = username,
			email = self.normalize_email(email),
			**kwargs
		)

		user.set_password(password)
		user.save(using=self._db)
		return user
	
	def create_superuser(self, first_name, last_name, username, email, password=None, **kwargs):
		"""The `**kwargs` is included to accept other keyword argument, even though it is not in this way in the django default create_superuser method of user class
		"""

		user = self.create_user(
			first_name = first_name,
			last_name = last_name,
			username = username,
			email = self.normalize_email(email),
			password = password,
			**kwargs
		)

		user.is_superuser = True
		user.is_staff = True
		user.save(using=self._db)
		return user
	

class UserAccount(AbstractBaseUser):
	"""Custom users account table (custom user model)"""

	first_name = models.CharField(max_length=100, unique=False)
	last_name = models.CharField(max_length=100, unique=False)
	username = models.CharField(max_length=255, unique=True)
	email = models.EmailField(max_length=255, unique=True)


	# `date_joined` below is not editable.
	# date_joined = models.DateTimeField(auto_now_add=True) # date_joined (not editable)
	
	# `last_modified` below is not editable.
	# last_modified = models.DateTimeField(auto_now=True) # last modified (not editable)

	# the default `last_login` for users is editable.

	# `pub_date` below is editable.
	# pub_date = models.DateTimeField(default=timezone.now) # (editable)


	# Default django permissions (is_active, is_staff, is_superuser)

	# Designates whether this user account should be considered active.
	# We recommend that you set this flag to False instead of deleting accounts;
	# that way, if your applications have any foreign keys to users, the foreign keys won`t break.
	is_active = models.BooleanField(default=True)

	# Designates whether the user can log into this admin site.
	is_staff = models.BooleanField(default=False)

	# Designates that this user has all permissions without explicitly assigning them.
	is_superuser = models.BooleanField(default=False)
	
	objects = UserAccountManager()
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['first_name', 'last_name', 'email']
	
	def __str__(self):
		return self.username
	
	def has_perm(self, perm, obj=None):
		return True
	
	def has_module_perms(self, app_label):
		return True
	

# NOTE: Whenever blank=True and null=True is used in a models.py field, make sure to replace it with required=False in forms.py field or in html file.


class Messages(models.Model):
	"""Messages table"""

	timestamp = models.DateTimeField(default=timezone.now)
	full_name = models.CharField(max_length=255, blank=False, null=False)
	email = models.CharField(max_length=255, blank=False, null=False)
	text_body = models.TextField(blank=False, null=False)
	is_read = models.BooleanField(default=False)
	
	def __str__(self):
		return f'{self.full_name} message sent on {self.timestamp}'
	

class Search(models.Model):
	"""Search table"""

	search_text = models.TextField(blank=False, null=False)
	timestamp = models.DateTimeField(default=timezone.now)
	is_seen = models.BooleanField(default=False)
	
	def __str__(self):
		return 'A search of {} on {}'.format(self.search_text, self.timestamp)
	

class Metrix(models.Model):
	"""Metrix table"""

	visit_num = models.IntegerField(default=0)
	timestamp = models.DateTimeField(default=timezone.now)
	is_seen = models.BooleanField(default=False)
	
	@property
	def slice_timestamp(self):
		"""Matrix timestamp"""
		
		timestamp_slice = str(self.timestamp)[:10] # 2022-10-18
		the_year = str(timestamp_slice[:4]) # slicing month only, from `timestamp_slice`
		slc_month = str(timestamp_slice[5:7]) # slicing month only, from `timestamp_slice`
		
		if slc_month == '01':
			the_month = 'january'
		elif slc_month == '02':
			the_month = 'february'
		elif slc_month == '03':
			the_month = 'march'
		elif slc_month == '04':
			the_month = 'april'
		elif slc_month == '05':
			the_month = 'may'
		elif slc_month == '06':
			the_month = 'june'
		elif slc_month == '07':
			the_month = 'july'
		elif slc_month == '08':
			the_month = 'august'
		elif slc_month == '09':
			the_month = 'september'
		elif slc_month == '10':
			the_month = 'october'
		elif slc_month == '11':
			the_month = 'november'
		elif slc_month == '12':
			the_month = 'december'
		else:
			the_month = 'ERROR WHILE SLICING'
		return [the_month, the_year]
	
	def __str__(self):
		return f'Metrix table, we have total of \'{self.visit_num}\' visitors, in {self.slice_timestamp[0]}, {self.slice_timestamp[1]}'
	

class Visitors(models.Model):
	"""Visitors table"""

	metrix = models.ForeignKey(Metrix, on_delete=models.CASCADE)
	ip_address = models.CharField(max_length=255, blank=False, null=False, default='0.0.0.0')
	timestamp = models.DateTimeField(default=timezone.now)
	is_seen = models.BooleanField(default=False)
	
	def __str__(self):
		return 'New visitor from {} on {}, of {}'.format(self.ip_address, self.timestamp, self.metrix.id)
