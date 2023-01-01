from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from account.default import Default, default
from django.core.paginator import Paginator
from blog.models import Category
from .forms import CategoryForm
from blog.post.forms import PostForm

from itertools import zip_longest


class Article:
  """
    article class which include article functionalities, from creating, viewing,
    updating, and deleting an article
  """
  
  @staticmethod
  def create(request):
    """this view handle the creation of an article"""
    if request.user.is_authenticated:
      if request.method == 'POST':
        form = CategoryForm(request.POST)
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
          
          get_article = instance.id
          messages.success(request, f'You successfully create an article.')
          return redirect(reverse('article:article', kwargs={'get_article': get_article}))
      else:
        form = CategoryForm()
      context = {
        'default': default(),
        'form': form
      }
      return render(request, 'blog/article/create.html', context)
    return False
  
  
  @staticmethod
  def article(request, get_article):
    """
      this an article page, and also it include creating new post,
      where it will be in the article list of post
    """
    article = Category.objects.get(id=get_article)
    article_all = article.post_set.all().order_by('-pub_date')
    real_url = Default.blog_url_processed(article)
    
    # here is the start tricks for creating post for this article
    if request.user.is_authenticated:
      if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
          url_list_name = form.cleaned_data.get('url_list_name')
          url_list_value = form.cleaned_data.get('url_list_value')
          list_1 = list(url_list_name.split(','))
          list_2 = list(url_list_value.split(','))
          url_list_data = list(zip_longest(list_1, list_2, fillvalue='Link'))
          
          instance = form.save(commit=False)
          instance.author = request.user
          instance.category = article
          
          # checking the form `url list` components
          if url_list_value == None or url_list_value == '' or url_list_name == None or url_list_name == '':
            instance.url_list = None
          else:
            instance.url_list = url_list_data
          instance.save()
          
          get_article = article.id
          messages.success(request, f'You successfully create a post.')
          return redirect(reverse('article:article', kwargs={'get_article': get_article}))
        messages.warning(request, f'Something went bad while creating a post.')
    
    paginator = Paginator(article_all, 5)
    page = request.GET.get('page')
    article_post = paginator.get_page(page)
    
    context = {
        'default': default(),
        'article': article,
        'article_post': article_post,
        'real_url': real_url
    }
    return render(request, 'blog/article.html', context)
  
  
  @staticmethod
  def update(request, get_article):
    """this is article update view"""
    article = Category.objects.get(id=get_article)
    real_url = Default.blog_url_processed(article)
    
    if request.user.is_authenticated:
      if request.method == 'POST':
        form = CategoryForm(request.POST, instance=article)
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
          
          get_article = instance.id
          messages.success(request, f'Successfully updated an article.')
          return redirect(reverse('article:article', kwargs={'get_article': get_article}))
      else:
        form = CategoryForm(instance=article)
      context = {
        'default': default(),
        'form': form,
        'real_url': real_url
      }
      return render(request, 'blog/article/update.html', context)
    return False