from django.urls import path
from .views import Search, Visitors, Notification


app_name = 'info'

urlpatterns = [
    path("search/", Search.search, name='search'),
    path("delete/search/<int:search_id>/", Search.delete, name='delete'),
    path("mark/search/<int:search_id>/", Search.markSearch, name='mark'),
    
    # visitor
    path("delete/visitor/<int:visitor_id>/", Visitors.delete, name='delete_visit'),
    path("mark/visitor/<int:visitor_id>/", Visitors.markVisitor, name='mark_visit'),
    
    # notification
    path("notification/", Notification.notification, name='notification'),
]
