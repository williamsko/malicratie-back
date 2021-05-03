# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models



class PartnerAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'brand_name',
        'logo',
        'created_at',
        'modified_at',
        'status',
    )
    list_filter = (
        'created_at',
        'modified_at',
        'status',
        'id',
        'brand_name',
        'logo',
        'created_at',
        'modified_at',
        'status',
    )
    date_hierarchy = 'created_at'


class AboutAdmin(admin.ModelAdmin):

    list_display = ('id', 'about', 'created_at', 'modified_at', 'status')
    list_filter = (
        'created_at',
        'modified_at',
        'status',
        'id',
        'about',
        'created_at',
        'modified_at',
        'status',
    )
    date_hierarchy = 'created_at'


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Partner, PartnerAdmin)
_register(models.About, AboutAdmin)
