from django.urls import path, include
from .views import Landing


urlpatterns = [
    path("", Landing.landing, name='landing'),
    path("", include('account.about.urls')),
    path("", include('account.auth.urls')),
    path("", include('account.info.urls')),
    path("", include('account.message.urls')),
]
