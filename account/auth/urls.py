# -*- coding: utf-8 -*-
from django.urls import path
from .views import (
	LoginCustom,
	LogoutCustom,
	change_password,
	about,
	notification,
	MessageCls,
	SearchCls,
	VisitorsCls)


app_name = 'auth'

urlpatterns = [
	path('login/', LoginCustom.as_view(template_name='account/login.html'), name='login'),
	path('logout/', LogoutCustom.as_view(template_name='account/logout.html'), name='logout'),
	path('change/password/', change_password, name='change_password'),
	path('about/', about, name='about'),
	path('notification/', notification, name='notification'),
	
	path('direct/message/', MessageCls.direct_message, name='direct_message'),
	path('message/send/', MessageCls.send, name='send_message'),
	path('mark/message/<int:msg_id>/', MessageCls.mark, name='mark_message'),
	path('delete/message/<int:msg_id>/', MessageCls.delete, name='delete_message'),
	
	path('search/', SearchCls.search, name='search'),
	path('mark/search/<int:search_id>/', SearchCls.mark, name='mark_search'),
	path('delete/search/<int:search_id>/', SearchCls.delete, name='delete_search'),
	
	path('mark/visitor/<int:visitor_id>/', VisitorsCls.mark, name='mark_visit'),
	path('delete/visitor/<int:visitor_id>/', VisitorsCls.delete, name='delete_visit'),
]
