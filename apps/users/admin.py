
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class ProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'type')
    list_filter = ('user', 'user', 'type')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Profile, ProfileAdmin)
