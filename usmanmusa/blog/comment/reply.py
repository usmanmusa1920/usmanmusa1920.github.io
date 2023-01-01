from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages
from blog import models



class Reply:
  """
    reply class which include reply functionalities, from creating,
    mark comment as read, and deleting a reply
  """
  
  
  @staticmethod
  def delete(request, reply_id):
    """delete reply view"""
    if request.user.is_authenticated:
      reply = models.Reply.objects.get(id=reply_id)
      reply.delete()
      messages.succes(request, f'Successfully deleted 1 reply.')
      return redirect(reverse('info:notification'))
    return False
  
  
  @staticmethod
  def markReply(request, reply_id):
    """mark reply as read view"""
    if request.user.is_authenticated:
      reply = models.Reply.objects.get(id=reply_id)
      reply.is_read = True
      reply.save()
      messages.succes(request, f'Successfully marked 1 reply as seen.')
      return redirect(reverse('info:notification'))
    return False