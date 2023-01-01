from django.urls import reverse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from account.default import default
from blog import models
from .forms import ReplyForm



class Comment:
  """
    comment class which include comment functionalities,
    from creating, mark comment as read, and deleting a comment
  """
  
  
  @staticmethod
  def comment(request, comment_id):
    """this view handle comment page"""
    comment = models.Comment.objects.get(id=comment_id)
    reply_all = comment.reply_set.all().order_by('-timestamp')
    if request.method == 'POST':
      form = ReplyForm(request.POST)
      if form.is_valid():
        name = form.cleaned_data.get('full_name')
        instance = form.save(commit=False)
        instance.comment = comment
        instance.save()
        messages.success(request, f'Welldone {name} for your reply.')
        return redirect(reverse('comment:comment', kwargs={'comment_id': comment_id}))
    else:
      form = ReplyForm()
    
    paginator = Paginator(reply_all, 5)
    page = request.GET.get('page')
    comment_reply = paginator.get_page(page)
    
    context = {
      'default': default(),
      'comment': comment,
      'comment_reply': comment_reply,
    }
    return render(request, 'blog/comment.html', context)
  
  
  @staticmethod
  def delete(request, comment_id):
    """comment delete view"""
    if request.user.is_authenticated:
      comment = models.Comment.objects.get(id=comment_id)
      comment.delete()
      messages.success(request, f'Successfully deleted 1 comment.')
      return redirect(reverse('info:notification'))
    return False
  
  
  @staticmethod
  def markComment(request, comment_id):
    """mark comment as read view"""
    if request.user.is_authenticated:
      comm = models.Comment.objects.get(id=comment_id)
      comm.is_read = True
      comm.save()
      messages.success(request, f'Successfully marked 1 comment as seen.')
      return redirect(reverse('info:notification'))
    return False