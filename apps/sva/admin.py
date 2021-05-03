# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class ParametrageAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'ip_adress',
        'operateur',
        'created_at',
        'modified_at',
    )
    list_filter = (
        'created_at',
        'modified_at',
        'id',
        'ip_adress',
        'operateur',
        'created_at',
        'modified_at',
    )
    date_hierarchy = 'created_at'


class OperateurAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'reference',
        'name',
        'created_at',
        'modified_at',
        'status',
    )
    list_filter = (
        'created_at',
        'modified_at',
        'status',
        'id',
        'reference',
        'name',
        'created_at',
        'modified_at',
        'status',
    )
    search_fields = ('name',)
    date_hierarchy = 'created_at'


class SmsResponseParameterAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'meaning', 'created_at', 'modified_at')
    list_filter = (
        'created_at',
        'modified_at',
        'id',
        'name',
        'meaning',
        'created_at',
        'modified_at',
    )
    search_fields = ('name',)
    date_hierarchy = 'created_at'


class SmsReceivedAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'number',
        'sms_content',
        'created_at',
        'modified_at',
    )
    list_filter = (
        'created_at',
        'modified_at',
        'id',
        'number',
        'sms_content',
        'created_at',
        'modified_at',
    )
    date_hierarchy = 'created_at'


class UssdRequestAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'meaning', 'created_at', 'modified_at')
    list_filter = (
        'created_at',
        'modified_at',
        'id',
        'name',
        'meaning',
        'created_at',
        'modified_at',
    )
    search_fields = ('name',)
    date_hierarchy = 'created_at'


class UssdResponseParameterAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'response', 'created_at', 'modified_at')
    list_filter = (
        'created_at',
        'modified_at',
        'id',
        'name',
        'response',
        'created_at',
        'modified_at',
    )
    search_fields = ('name',)
    date_hierarchy = 'created_at'


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Parametrage, ParametrageAdmin)
_register(models.Operateur, OperateurAdmin)
_register(models.SmsResponseParameter, SmsResponseParameterAdmin)
_register(models.SmsReceived, SmsReceivedAdmin)
_register(models.UssdRequest, UssdRequestAdmin)
_register(models.UssdResponseParameter, UssdResponseParameterAdmin)
