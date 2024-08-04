from django.contrib import admin
from .models import (
	Category,
	Post,
	Comment,
	Reply)


class PostInline(admin.TabularInline):
	"""Post inline, which will show when view metrix via admin at bottom"""

	# post model
	model = Post
	
	# making it to be zero profile for a user, it can be one (1) or more
	extra = 0


class CategoryAdmin(admin.ModelAdmin):
	"""Category admin customisation"""

	search_fields = (
		'publisher',
		'pub_date',
		'title',
		'image_url',
		'last_modified',
		'description',
		'snippet',
	)
	ordering = ('-last_modified',)

	list_filter = (
		'publisher',
		'pub_date',
		'title',
		'last_modified'
	)

	list_display = (
		'title',
		'publisher',
		'pub_date',
		'last_modified'
	)

	fieldsets = (
		(None, {'fields': ('publisher', 'title', 'image_url', 'description', 'snippet',),}),
		('Date Information', {'fields':('pub_date',)}),
	)
	inlines = [PostInline]


class CommentInline(admin.TabularInline):
	"""Comment inline, which will show when view metrix via admin at bottom"""

	# comment model
	model = Comment
	
	# making it to be zero profile for a user, it can be one (1) or more
	extra = 0
	

class PostAdmin(admin.ModelAdmin):
	"""Post admin customisation"""
	
	search_fields = (
		'category',
		'author',
		'pub_date',
		'title',
		'image_url',
		'last_modified',
		'summary',
		'snippet',
	)
	ordering = ('-last_modified',)

	list_filter = (
		'author',
		'pub_date',
		'title',
		'last_modified'
	)

	list_display = (
		'title',
		'category',
		'author',
		'pub_date',
		'last_modified',
		'last_modified'
	)

	fieldsets = (
		(None, {'fields': ('category', 'author', 'title', 'image_url', 'summary', 'snippet',),}),
		('Date Information', {'fields':('pub_date',)}),
	)
	inlines = [CommentInline]


class ReplyInline(admin.TabularInline):
	"""Reply inline, which will show when view metrix via admin at bottom"""

	# reply model
	model = Reply
	
	# making it to be zero profile for a user, it can be one (1) or more
	extra = 0
	

class CommentAdmin(admin.ModelAdmin):
	"""Comment admin customisation"""
	
	search_fields = (
		'full_name',
		'email',
		'text_body',
		'timestamp',
		'is_read'
	)
	ordering = ('-timestamp',)

	list_filter = (
		'full_name',
		'email',
		'timestamp',
		'is_read'
	)

	list_display = (
		'full_name',
		'email',
		'text_body',
		'post',
		'timestamp',
		'is_read'
	)

	fieldsets = (
		(None, {'fields': ('post', 'full_name', 'email', 'text_body',),}),
		('Date Information', {'fields':('timestamp',)}),
	)
	inlines = [ReplyInline]


class ReplyAdmin(admin.ModelAdmin):
	"""Reply admin customisation"""
	
	search_fields = (
		'full_name',
		'email',
		'text_body',
		'timestamp',
		'is_read'
	)
	ordering = ('-timestamp',)

	list_filter = (
		'full_name',
		'timestamp',
		'is_read'
	)

	list_display = (
		'full_name',
		'email',
		'text_body',
		'comment',
		'timestamp',
		'is_read'
	)

	fieldsets = (
		(None, {'fields': ('comment', 'full_name', 'email', 'text_body',),}),
		('Date Information', {'fields':('timestamp',)}),
	)
	inlines = []

	
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Reply, ReplyAdmin)
