from django.urls import path
from .views import About


app_name = 'about'

urlpatterns = [
    path("about/", About.about, name='about'),
]
