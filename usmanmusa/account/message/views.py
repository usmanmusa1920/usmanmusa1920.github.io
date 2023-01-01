from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages
from account.models import Messages
from account.message.forms import MessageForm



class Message:
  """
    message class which include message functionalities, from creating, viewing,
    editing, and deleting a message
  """
  
  @staticmethod
  def send(request):
    """send message view"""
    if request.method == 'POST':
      form = MessageForm(request.POST)
      if form.is_valid():
        name = form.cleaned_data.get('full_name')
        form.save()
        messages.success(request, f'Thanks "{name}" for your message, Usman will response at the earliest.')
        return redirect('landing')
      else:
        messages.warning(request, f'OOPs something went wrong, {name} try sending later.')
    else:
      form = MessageForm(request.POST)
    return False
  
  
  @staticmethod
  def markMessage(request, msg_id):
    """mark message as read view"""
    if request.user.is_authenticated:
      msg = Messages.objects.get(id=msg_id)
      msg.is_read = True
      msg.save()
      messages.success(request, f'Successfully marked 1 message as seen.')
      return redirect(reverse('info:notification'))
    return False
  
  
  @staticmethod
  def deleteMessage(request, msg_id):
    """delete a message view"""
    if request.user.is_authenticated:
      msg = Messages.objects.get(id=msg_id)
      msg.delete()
      messages.success(request, f'Successfully deleted 1 message.')
      return redirect(reverse('info:notification'))
    return False