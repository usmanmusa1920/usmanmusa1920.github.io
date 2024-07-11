from django.shortcuts import render, redirect
from .default import general_context, Viz


class Landing:
    """
    Landing class
    """

    @staticmethod
    def landing(request):
        """landing page view"""

        if request.user.is_authenticated:
            # escape adding authenticated user as a visitor (if login), only other who visit without login
            pass
        else:
            # who so ever visit the site without being logged in, will be added as a visitor, into the database, (the below called class method handle the functionalities)
            Viz.vizFun()
        return redirect('blog:blog')
    

# General context for error pages
context = {
    'general_context': general_context(),
}


def error_400(request, exception):
    """This view handle 400 error"""
    
    # Page 400 bad request
    return render(request, 'account/_400.html', context=context)


def error_403(request, exception):
    """This view handle 403 error"""
    
    # Page 403 forbidden (permission denied)
    return render(request, 'account/_403.html', context=context)


def error_404(request, exception):
    """This view handle 404 error"""
    
    # Page 404 not found
    return render(request, 'account/_404.html', context=context)


def error_500(request):
    """This view handle 500 error"""
    
    # Page 500 internal server error
    return render(request, 'account/_500.html', context=context)
