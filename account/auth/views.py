# -*- coding: utf-8 -*-
from django.db.models import Q
from django.urls import reverse
from django.contrib import messages
from django.utils.html import format_html
from django.core.paginator import Paginator
from django.shortcuts import (
	render,
	redirect)
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
	LoginView,
	LogoutView)
from account.models import (
	Messages,
	Search,
	Visitors,
	Metrix)
from account.default import (
	integrate_mail,
	general_context)
from account.forms import MessageForm
from blog.models import (
	Post,
	Comment,
	Reply)
from .forms import PasswordChangeForm


class LoginCustom(LoginView):
	"""Account login class"""

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		current_site = get_current_site(self.request)

		context.update({
			'general_context': general_context(),
			self.redirect_field_name: self.get_redirect_url(),
			'site': current_site,
			'site_name': current_site.name,
			**(self.extra_context or {})
		})
		return context
	

class LogoutCustom(LoginRequiredMixin ,LogoutView):
	"""Account logout class"""

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		current_site = get_current_site(self.request)

		context.update({
			'general_context': general_context(),
			'site': current_site,
			'site_name': current_site.name,
			# 'title': _('Logged out'),
			**(self.extra_context or {})
		})
		return context
	

@login_required
def change_password(request):
	"""Password change view"""
	
	form = PasswordChangeForm(user=request.user, data=request.POST or None)
	if form.is_valid():
		form.save()
		update_session_auth_hash(request, form.user)
		messages.success(request, f'That sound great {request.user.first_name}, your password has been changed')
		return redirect(reverse('landing'))
	
	context = {
		'general_context': general_context(),
		'form': form
	}
	return render(request, 'account/change_password.html', context=context)


def about(request):
	"""About page view"""
	
	return render(request, 'account/about.html', context={'general_context': general_context()})


@login_required
def notification(request):
	"""This class method give us a list of recent post comments, replies, searchs, visitors and messages that are sent."""
	
	comment_all = Comment.objects.filter(is_read=False).order_by('-timestamp')
	reply_all = Reply.objects.filter(is_read=False).order_by('-timestamp')
	search_all = Search.objects.filter(is_seen=False).order_by('-timestamp')
	visit_all = Visitors.objects.filter(is_seen=False).order_by('-timestamp')
	message_all = Messages.objects.filter(is_read=False).order_by('-timestamp')
	
	# comments pagination
	paginator_1 = Paginator(comment_all, 5)
	page = request.GET.get('page')
	comments = paginator_1.get_page(page)
	
	# replys pagination
	paginator_2 = Paginator(reply_all, 5)
	page = request.GET.get('page')
	replys = paginator_2.get_page(page)
	
	# searches pagination
	paginator_3 = Paginator(search_all, 5)
	page = request.GET.get('page')
	searches = paginator_3.get_page(page)
	
	# visitors pagination
	paginator_4 = Paginator(visit_all, 5)
	page = request.GET.get('page')
	visitors = paginator_4.get_page(page)
	
	# messages paginations
	paginator_5 = Paginator(message_all, 5)
	page = request.GET.get('page')
	msgs = paginator_5.get_page(page)
	
	context = {
		'general_context': general_context(),
		'comments': comments,
		'replys': replys,
		'searches': searches,
		'visitors': visitors,
		'Messages': msgs,
	}
	return render(request, 'account/notification.html', context=context)


class MessageCls:
	"""Message class which include method for sending, viewing, editing, and deleting a message."""

	@staticmethod
	def direct_message(request):
		"""Direct message view"""
		
		context = {'general_context': general_context()}
		return render(request, 'account/direct_message.html', context=context)
	
	@staticmethod
	def send(request):
		"""Send message view"""
		
		form = MessageForm(request.POST)
		if form.is_valid():
			sender_name = form.cleaned_data.get('full_name')
			sender_email = form.cleaned_data.get('email')
			text_body = form.cleaned_data.get('text_body')
			integrate_mail(sender_name, sender_email, text_body)
			
			form.save()
			messages.success(
				request, format_html('Thanks<b>&nbsp;{}&nbsp;</b>for your message,&nbsp;<b>Usman</b>&nbsp;will response at the earliest.', sender_name))
			return redirect('auth:direct_message')
		
	@login_required
	@staticmethod
	def mark(request, msg_id):
		"""Mark message as read view"""
		
		msg = Messages.objects.get(id=msg_id)
		msg.is_read = True
		msg.save()
		messages.success(request, f'Successfully marked 1 message as seen.')
		return redirect(reverse('auth:notification'))
	
	@login_required
	@staticmethod
	def delete(request, msg_id):
		"""Delete a message view"""
		
		msg = Messages.objects.get(id=msg_id)
		msg.delete()
		messages.success(request, f'Successfully deleted 1 message.')
		return redirect(reverse('auth:notification'))
	

class SearchCls:
	"""Search class which includes: searching, deleting, and mark search as read."""

	@staticmethod
	def search(request):
		"""Search view"""

		search_panel = request.GET.get('search_q')

		if search_panel == None or search_panel == '' or search_panel == ' ' or search_panel == '  ' or search_panel == '   ' or search_panel == '	' or search_panel == '	 ':
			pass
		else:
			history = Search(search_text=search_panel)
			history.save()

		# This try and except block, is a filter that filter blog post matching a giving query, it try to see if a giving quey (starts_with or contains) for the search item in the database, and the reason is that by default the input field of the search is 'None' so when ever it query 'None' it will give an error so the except block handle it.
		try:
			posts_search = Post.objects.filter(Q(title__istartswith=search_panel) | Q(title__contains=search_panel) | Q(summary__istartswith=search_panel) | Q(summary__contains=search_panel) | Q(snippet__istartswith=search_panel) | Q(snippet__contains=search_panel)).order_by('-last_modified')
		except:
			posts_search = Post.objects.filter(Q(title=search_panel) | Q(summary=search_panel) | Q(snippet=search_panel)).order_by('-last_modified')

		paginator = Paginator(posts_search, 7)
		page = request.GET.get('page')
		posts = paginator.get_page(page)

		context = {
			'general_context': general_context(),
			'posts': posts,
			'search_panel': search_panel,
		}
		return render(request, 'account/search.html', context=context)
	
	@login_required
	@staticmethod
	def delete(request, search_id):
		"""Delete a search"""
		
		serch = Search.objects.get(id=search_id)
		serch.delete()
		messages.success(request, f'Successfully deleted 1 search.')
		return redirect(reverse('auth:notification'))
	
	@login_required
	@staticmethod
	def mark(request, search_id):
		"""Mark search as read"""
		
		serch = Search.objects.get(id=search_id)
		serch.is_seen = True
		serch.save()
		messages.success(request, f'Successfully marked 1 search as seen.')
		return redirect(reverse('auth:notification'))
	

class VisitorsCls:
	"""Visitors class"""

	@login_required
	@staticmethod
	def delete(request, visitor_id):
		"""Delete a visitor"""
		
		visit = Visitors.objects.get(id=visitor_id)
		visitor_metrix = Metrix.objects.get(id=visit.metrix.id)
		
		# reduce the number of visitors per metrix once a visitor is deleted
		visitor_metrix.visit_num -= 1
		visitor_metrix.save()
		visit.delete()
		
		messages.success(request, f'Successfully deleted 1 visitor.')
		return redirect(reverse('auth:notification'))
	
	@login_required
	@staticmethod
	def mark(request, visitor_id):
		"""Mark visitor as read"""
		
		visit = Visitors.objects.get(id=visitor_id)
		visit.is_seen = True
		visit.save()
		messages.success(request, f'Successfully marked 1 visitor as read.')
		return redirect(reverse('auth:notification'))
