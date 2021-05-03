# vim: set fileencoding=utf-8 :
from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from . import models


class GeoAdmin(DjangoMpttAdmin):

    list_display = (
        'id',
        'name',
        'code',
        'type',
        'lon',
        'lat',
        'parent',
        'nb_hbts',
        
    )

    list_filter = (
        'type',
    )
    
    search_fields = ('name','id')
    date_hierarchy = 'created_at'


class PDECSInline(admin.TabularInline):
    model = models.PDECSDetailedBudget
    extra = 1


class PDECSAdmin(admin.ModelAdmin):

    inlines = [PDECSInline]

    list_display = (
        'id',
        'name',
        'reference',
        'budget',
        'geo',
        'fichier_pdsec',
        'created_at',
        'modified_at',
    )
    list_filter = (
        'geo',
        'created_at',
        'modified_at',
        'id',
        'name',
        'reference',
        'budget',
        'geo',
        'fichier_pdsec',
        'created_at',
        'modified_at',
    )
    search_fields = ('name',)
    date_hierarchy = 'created_at'






def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Geo, GeoAdmin)
_register(models.PDECS, PDECSAdmin)
