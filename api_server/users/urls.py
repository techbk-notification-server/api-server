from django.conf.urls import url
from .views import LogInView
app_name = 'users'

urlpatterns = [
    url(r'^login/$', LogInView.as_view(), name= 'login'),
    # url(r'logout$', , ),
]