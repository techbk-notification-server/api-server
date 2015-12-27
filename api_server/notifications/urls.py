from django.conf.urls import url
from .views import JsonNotificationsView
app_name = 'notifications'

urlpatterns = [
    url(r'', JsonNotificationsView.as_view(), name= 'noti'),
    # url(r'logout$', , ),
]