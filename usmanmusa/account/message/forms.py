from django import forms
from account.models import Messages


class MessageForm(forms.ModelForm):
  
  class Meta:
    model = Messages
    fields = ['full_name', 'email', 'text_body']