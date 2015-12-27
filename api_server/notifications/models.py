from django.db import models
from django.contrib.auth.models import User


class StartUrl(models.Model):
    """

    """
    url = models.URLField()
    description = models.CharField(max_length=100)
    user = models.ManyToManyField(User, through='UserWeb', through_fields=('start_url','user'))

    def __str__(self):
        return "%s : %s" % (self.description, self.url)


class UserWeb(models.Model):
    """

    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_url = models.ForeignKey(StartUrl, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.BooleanField(default=True)

    class Meta:
        unique_together = ('user', 'start_url')

class NewsNotification(models.Model):
    """

    """
    start_url = models.ForeignKey(StartUrl, on_delete=models.CASCADE)
    url = models.URLField()
    title = models.TextField(default="No title")
    checked = models.BooleanField(default=False)
