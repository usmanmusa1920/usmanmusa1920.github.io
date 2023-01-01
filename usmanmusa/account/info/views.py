from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from account.default import default
from account import models
from blog.models import Post, Comment, Reply



class Search:
  """
    search class which include search functionalities, from searching,
    deleting, and mark_as_read of a search
  """
  
  
  @staticmethod
  def search(request):
    """search view"""
    search_panel = request.GET.get('search_q')
  
    if search_panel == None or search_panel == '' or search_panel == ' ' or search_panel == '  ' or search_panel == '   ' or search_panel == '    ' or search_panel == '     ':
      pass
    else:
      history = models.Search(search_text=search_panel)
      history.save()
      
    """
      This try and except block, is a filter that filter blog post matching a giving query, it try to see if a giving quey (starts_with or contains) for the search item in the database, and the reason is that by default the input field of the search is 'None' so when ever it query 'None' it will give an error so the except block handle it
    """
    try:
      posts_search = Post.objects.filter(Q(title__istartswith=search_panel) | Q(title__contains=search_panel) | Q(summary__istartswith=search_panel) | Q(summary__contains=search_panel) | Q(snippet__istartswith=search_panel) | Q(snippet__contains=search_panel)).order_by('-last_modified')
    except:
      posts_search = Post.objects.filter(Q(title=search_panel) | Q(summary=search_panel) | Q(snippet=search_panel)).order_by('-last_modified')
    paginator = Paginator(posts_search, 7)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
      'default': default(),
      'posts': posts,
      'search_panel': search_panel,
    }
    return render(request, 'account/search.html', context)
  
  
  @staticmethod
  def delete(request, search_id):
    """delete a search"""
    if request.user.is_authenticated:
      serch = models.Search.objects.get(id=search_id)
      serch.delete()
      messages.success(request, f'Successfully deleted 1 search.')
      return redirect(reverse('info:notification'))
    return False
  
  
  @staticmethod
  def markSearch(request, search_id):
    """mark search as read"""
    if request.user.is_authenticated:
      serch = models.Search.objects.get(id=search_id)
      serch.is_seen = True
      serch.save()
      messages.success(request, f'Successfully marked 1 search as seen.')
      return redirect(reverse('info:notification'))
    return False
  
  
class Visitors:
  
  @staticmethod
  def delete(request, visitor_id):
    """delete a visitor"""
    if request.user.is_authenticated:
      visit = models.Visitors.objects.get(id=visitor_id)
      visitor_metrix = models.Metrix.objects.get(id=visit.metrix.id)
      
      """
        we reduce the number of visitors per metrix
        once a visitor is deleted
      """
      visitor_metrix.visit_num -= 1
      visitor_metrix.save()
      
      visit.delete()
      
      messages.success(request, f'Successfully deleted 1 visitor.')
      return redirect(reverse('info:notification'))
    return False
  
  
  @staticmethod
  def markVisitor(request, visitor_id):
    """mark visitor as read"""
    if request.user.is_authenticated:
      visit = models.Visitors.objects.get(id=visitor_id)
      visit.is_seen = True
      visit.save()
      messages.success(request, f'Successfully marked 1 visitor as read.')
      return redirect(reverse('info:notification'))
    return False
  
  
class Notification:
  
  @staticmethod
  def notification(request):
    """
      this class method it will give us a list of recent post comments,
      replies, searchs, visitors and messages sent.
    """
    if request.user.is_authenticated:
      comment_all = Comment.objects.filter(is_read=False).order_by('-timestamp')
      reply_all = Reply.objects.filter(is_read=False).order_by('-timestamp')
      search_all = models.Search.objects.filter(is_seen=False).order_by('-timestamp')
      visit_all = models.Visitors.objects.filter(is_seen=False).order_by('-timestamp')
      message_all = models.Messages.objects.filter(is_read=False).order_by('-timestamp')
      
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
      Messages = paginator_5.get_page(page)
      
      context = {
        'default': default(),
        'comments': comments,
        'replys': replys,
        'searches': searches,
        'visitors': visitors,
        'Messages': Messages
      }
      return render(request, 'account/notification.html', context)
    return False