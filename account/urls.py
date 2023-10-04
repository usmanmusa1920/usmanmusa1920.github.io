from django.urls import path, include
from .views import Landing


urlpatterns = [
    path('', Landing.landing, name='landing'),
    path('', include('account.auth.urls')),
]
