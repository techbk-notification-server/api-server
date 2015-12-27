from django.views import generic
from .models import NewsNotification, StartUrl
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse


class NotificationsView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    template_name = 'notifications/notifications.html'
    model = NewsNotification
    context_object_name = 'notification'

    # def get_queryset(self):


# from django.http.request import HttpRequest

class JsonNotificationsView(LoginRequiredMixin, generic.View):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        notis = NewsNotification.objects.filter(start_url__user=request.user, start_url__userweb__status=True)
        data = [{"start_url": x.start_url.description, "title": x.title, "url": x.url, "status": x.checked}
                for x in notis]

        return JsonResponse(data, safe=False)
