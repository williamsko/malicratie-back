# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models



class QuestionsAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'reference',
        'question',
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
        'question',
        'created_at',
        'modified_at',
        'status',
    )
    date_hierarchy = 'created_at'


class CampaignAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'reference',
        'name',
        'campaign_date',
        'created_at',
        'modified_at',
        'status',
    )
    list_filter = (
        'campaign_date',
        'created_at',
        'modified_at',
        'status',
        'id',
        'reference',
        'name',
        'campaign_date',
        'created_at',
        'modified_at',
        'status',
    )
    filter_horizontal = ('questions',)
    search_fields = ('name',)
    date_hierarchy = 'created_at'


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Questions, QuestionsAdmin)
_register(models.Campaign, CampaignAdmin)
