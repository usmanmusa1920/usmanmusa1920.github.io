from django.shortcuts import render
from .default import default, Viz


class Landing:
  
  @staticmethod
  def landing(request):
    """landing page view"""
    if request.user.is_authenticated:
      """
        i don't want to add myself as a visitor, if i am login,
        only other who visit without login
      """
      pass
    else:
      """
        who so ever visit the site without login will be added as a visitor,
        into our database, (the below class method handle the functionalities)
      """
      Viz.vizFun()
      
    context = {
      'default': default(),
    }
    return render(request, 'account/landing.html', context)
  
  

def error_403(request, exception):
  """this view handle 403 error"""
  return render(request, 'account/error/_403.html')


def error_404(request, exception):
  """this view handle 404 error"""
  return render(request, 'account/error/_404.html')


def error_500(request):
  """this view handle 500 error"""
  return render(request, 'account/error/_500.html')