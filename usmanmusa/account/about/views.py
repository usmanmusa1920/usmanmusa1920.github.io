from django.shortcuts import render
from account.default import default


class About:
  """
    about class which include about page view
  """
  
  @staticmethod
  def about(request):
    """about page view"""
    context = {
      'default': default()
    }
    return render(request, 'account/about.html', context)