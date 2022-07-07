from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from .models import (
	Messages,
	Metrix,
	Visitors,
	Search)


User = get_user_model()


class UserAdminForm(UserAdmin):
	"""User admin page customisation"""

	# sets which model fields will be searched when a search is performed in django admin
	search_fields = (
		'username',
		'email',
	)
	
	# fields values that we can filter via admin (side-bar usually by right)
	list_filter = (
		'first_name',
		'last_name',
		'username',
		'email',
		'is_active',
		'is_superuser',
		'is_staff',
	)
	
	# list to display
	list_display = (
		'first_name',
		'last_name',
		'last_login',
		'username',
		'email',
		'is_active',
		'is_superuser',
		'is_staff',
	)
	
	# These are the field `fieldsets` that will display when you want to edit user account via admin.
	
	# Don`t put `last_modified` and `date_joined` in the below fieldset because they are not editable.

	# But `last_login` is editable, but don`t put it also, why? to avoid mistakely editing it for a user that is why it is commented out below.
	fieldsets = (
		(
			None, {
				'fields': (
					'password',
					'username',
					'email',
				)
			}
		),
		(
			'Personal', {
				'fields': (
					'first_name',
					'last_name',
				)
			}
		),
		# (
		#	 'Account activity', {
		#		 'fields': (
		#			 'last_login',
		#		 )
		#	 }
		# ),
		(
			'Permissions', {
				'fields': (
					'is_active',
					'is_superuser',
					'is_staff',
				)
			}
		),
	)
	
	# These are the field that will display when you want to create new user account via admin.
	add_fieldsets = (
		(
			None, {
				'classes':(
					'wide',
				),
				'fields':(
					'first_name',
					'last_name',
					'username',
					'email',
					'is_active',
					'is_superuser',
					'is_staff',
					'password1',
					'password2',
				)
			}
		),
	)
	
	# An interface for many-to-many relations, which allows the user to filter a list of available related objects. It is included to avoid error of the following, since we don`t have any many-to-many relation in our custome user model (we are not using defaul user model of django):
		# <class 'account.admin.UserAdminForm'>: (admin.E019) The value of 'filter_horizontal[0]' refers to 'groups', which is not a field of 'account.UserAccount'.
		# <class 'account.admin.UserAdminForm'>: (admin.E019) The value of 'filter_horizontal[1]' refers to 'user_permissions', which is not a field of 'account.UserAccount'.
	filter_horizontal = ()


class MessageAdmin(admin.ModelAdmin):
	"""Message admin customisation"""

	# sets which model fields will be searched when a search is performed in django admin
	search_fields = (
		'full_name',
		'email',
		'text_body',
		'timestamp',
		'is_read',
	)
	
	# how users will be ordered via admin
	ordering = ('-timestamp',)
	
	# fields values that we can filter via admin (side-bar usually by right)
	list_filter = (
		'full_name',
		'timestamp',
		'is_read',
	)
	
	# list to display
	list_display = (
		'full_name',
		'email',
		'text_body',
		'timestamp',
		'is_read',
	)
	
	# These are the field `fieldsets` that will display when you want to edit message via admin.
	fieldsets = (
		(None, {"fields": ('full_name', 'email', 'text_body'),}),
		('Date Information', {'fields':('timestamp', 'is_read')}),
	)


class SearchAdmin(admin.ModelAdmin):
	"""Search admin customisation"""

	# sets which model fields will be searched when a search is performed in django admin
	search_fields = ('search_text', 'timestamp', 'is_seen')
	
	# how users will be ordered via admin
	ordering = ('-timestamp',)
	
	# fields values that we can filter via admin (side-bar usually by right)
	list_filter = ('search_text', 'timestamp', 'is_seen')
	
	# list to display
	list_display = ('search_text', 'timestamp', 'is_seen')


class VisitorsInline(admin.TabularInline):
	"""Visitors inline, which will show when view metrix via admin at bottom"""

	# visitors model
	model = Visitors
	
	# making it to be zero profile for a user, it can be one (1) or more
	extra = 0


class MetrixAdmin(admin.ModelAdmin):
	"""Metrix admin customisation"""

	# sets which model fields will be searched when a search is performed in django admin
	search_fields = ('visit_num', 'timestamp', 'is_seen')
	
	# how users will be ordered via admin
	ordering = ('-timestamp',)
	
	# fields values that we can filter via admin (side-bar usually by right)
	list_filter = ('visit_num', 'timestamp', 'is_seen')
	
	# These are the field `fieldsets` that will display when you want to edit metrix via admin.
	fieldsets = (
		(None, {"fields": ('visit_num',),}),
		('Date Information', {'fields':('timestamp', 'is_seen')}),
	)
	
	# Including users profile forms when registering new user, so that to make it automatically create user profile, like that of the signals, but only if clicked.
	inlines = [VisitorsInline]


class VisitorsAdmin(admin.ModelAdmin):
	"""Visitors admin customisation"""

	# sets which model fields will be searched when a search is performed in django admin
	search_fields = ('ip_address', 'timestamp', 'is_seen')
	
	# how users will be ordered via admin
	ordering = ('-timestamp',)
	
	# fields values that we can filter via admin (side-bar usually by right)
	list_filter = ('ip_address', 'timestamp', 'is_seen')
	
	# list to display
	list_display = ('ip_address', 'timestamp', 'is_seen')


admin.site.index_title = 'Usman Musa administration'
admin.site.site_title = 'admin page'
# Usman Musa administration | admin page
admin.site.site_header = 'Usman Musa admin site'


admin.site.register(User, UserAdminForm)
admin.site.register(Messages, MessageAdmin)
admin.site.register(Metrix, MetrixAdmin)
admin.site.register(Visitors, VisitorsAdmin)
admin.site.register(Search, SearchAdmin)
admin.site.unregister(Group)
