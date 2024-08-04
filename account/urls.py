from django.urls import (
	path,
	include)
from .views import landing


urlpatterns = [
	path('', landing, name='landing'),
	path('', include('account.auth.urls')),
]
