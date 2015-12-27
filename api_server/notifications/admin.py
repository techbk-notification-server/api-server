from django.contrib import admin
from django.contrib.auth.models import User
from . import models


class NewsNotiInline(admin.TabularInline):
    model = models.NewsNotification
    # extra = 1


class WebsiteInline(admin.TabularInline):
    model = models.StartUrl
    # extra = 1

class UserWebInline(admin.TabularInline):
    model = models.UserWeb
    # extra = 1


class NewsNotification(admin.ModelAdmin):
    list_display = ('start_url', 'title', 'url', 'checked')


class UserWeb(admin.ModelAdmin):
    list_display = ('start_url', 'user', 'date', 'status')


class UserAdmin(admin.ModelAdmin):
    inlines = [UserWebInline]


class StartUrl(admin.ModelAdmin):
    list_display = ('url', 'description')
    inlines = [NewsNotiInline, UserWebInline]


admin.site.register(models.NewsNotification, NewsNotification)
admin.site.register(models.UserWeb, UserWeb)
admin.site.register(models.StartUrl, StartUrl)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
