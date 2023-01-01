from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from account.default import Default, default
from blog import models
from blog.post.forms import PostForm
from blog.comment.forms import CommentForm

from itertools import zip_longest



class Post:
  """
    post class which include post functionalities, from creating,
    updating, and deleting a post
  """
  
  
  @staticmethod
  def post(request, post_id):
    """view for post page"""
    post = models.Post.objects.get(id=post_id)
    real_url = Default.blog_url_processed(post)
    comments_all = post.comment_set.all().order_by('-timestamp')
    if request.method == 'POST':
      form = CommentForm(request.POST)
      if form.is_valid():
        name = form.cleaned_data.get('full_name')
        instance = form.save(commit=False)
        instance.post = post
        instance.save()
        messages.success(request, f'Welldone {name} for your comment.')
        return redirect(reverse('post:post', kwargs={'post_id': post_id}))
    else:
      form = CommentForm()
    
    paginator = Paginator(comments_all, 5)
    page = request.GET.get('page')
    post_comment = paginator.get_page(page)
    
    context = {
      'default': default(),
      'post': post,
      'post_comment': post_comment,
      'real_url': real_url
    }
    return render(request, 'blog/post.html', context)
  
  
  @staticmethod
  def update(request, post_id):
    """view for updating a post"""
    post = models.Post.objects.get(id=post_id)
    real_url = Default.blog_url_processed(post)
    
    if request.user.is_authenticated:
      if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
          url_list_name = form.cleaned_data.get('url_list_name')
          url_list_value = form.cleaned_data.get('url_list_value')
          list_1 = list(url_list_name.split(','))
          list_2 = list(url_list_value.split(','))
          url_list_data = list(zip_longest(list_1, list_2, fillvalue='Link'))
          
          instance = form.save(commit=False)
          instance.publisher = request.user
          
          # checking the form `url list` components
          if url_list_value == None or url_list_value == '' or url_list_name == None or url_list_name == '':
            instance.url_list = None
          else:
            instance.url_list = url_list_data
          instance.save()
          
          messages.success(request, f'Post is updated.')
          return redirect(reverse('post:post', kwargs={'post_id': post_id}))
      else:
        form = PostForm(instance=post)
      context = {
        'default': default(),
        'form': form,
        'real_url': real_url
      }
      return render(request, 'blog/post/update.html', context)
    return False
  
  
  @staticmethod
  def delete(request, post_id):
    """view for deleting a post"""
    if request.user.is_authenticated:
      post = models.Post.objects.get(id=post_id)
      post_article_id = post.category.id
      post.delete()
      messages.success(request, f'You successfully deleted "{post.title}" post.')
      return redirect(reverse('article:article', kwargs={'get_article':post_article_id}))
    return False