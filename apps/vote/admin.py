# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class VoteTypeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'code',
        'created_at',
        'modified_at',
        'status',
    )
    list_filter = (
        'created_at',
        'modified_at',
        'status',
        'id',
        'name',
        'code',
        'created_at',
        'modified_at',
        'status',
    )
    search_fields = ('name',)
    date_hierarchy = 'created_at'


class CandidateTypeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'code',
        'created_at',
        'modified_at',
        'status',
    )
    list_filter = (
        'created_at',
        'modified_at',
        'status',
        'id',
        'name',
        'code',
        'created_at',
        'modified_at',
        'status',
    )
    search_fields = ('name',)
    date_hierarchy = 'created_at'


class IncidentTypeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'code',
        'created_at',
        'modified_at',
        'status',
    )
    list_filter = (
        'created_at',
        'modified_at',
        'status',
        'id',
        'name',
        'code',
        'created_at',
        'modified_at',
        'status',
    )
    search_fields = ('name',)
    date_hierarchy = 'created_at'


class VoteAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'reference',
        'name',
        'type',
        'vote_date',
        'created_at',
        'modified_at',
        'status',
    )
    list_filter = (
        'type',
        'vote_date',
        'created_at',
        'modified_at',
        'status',
        'id',
        'reference',
        'name',
        'type',
        'vote_date',
        'created_at',
        'modified_at',
        'status',
    )
    search_fields = ('name',)
    date_hierarchy = 'created_at'


class CandidateAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'reference',
        'name',
        'type',
        'parti',
        'photo',
        'color',
        'created_at',
        'modified_at',
        'status',
    )
    list_filter = (
        'type',
        'created_at',
        'modified_at',
        'status',
        'id',
        'reference',
        'name',
        'type',
        'parti',
        'photo',
        'color',
        'created_at',
        'modified_at',
        'status',
    )
    search_fields = ('name',)
    date_hierarchy = 'created_at'


class VoteOfficeAdmin(admin.ModelAdmin):
    autocomplete_fields = ['geo_zone']

    list_display = (
        'id',
        'reference',
        'name',
        'geo_zone',
        'open_hour',
        'close_hour',
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
        'geo_zone',
        'created_at',
        'modified_at',
        'status',
    )
    search_fields = ('name',)
    date_hierarchy = 'created_at'


class ObserverAdmin(admin.ModelAdmin):
    autocomplete_fields = ['vote_office']

    list_display = (
        'id',
        'reference',
        'photo',
        'profile',
        'vote_office',
        'created_at',
        'modified_at',
        'status',
    )
    list_filter = (
        'profile',
        'vote_office',
        'status',
        'created_at',
        'modified_at',
        'status',
    )
    date_hierarchy = 'created_at'


class VoteResultAdmin(admin.ModelAdmin):
    autocomplete_fields = ['vote','vote_office']

    list_display = (
        'id',
        'reference',
        'vote',
        'vote_office',
        'observer',
        'subscribed_number',
        'voters_number',
        'spoiled_ballots',
        'abstention',
        'created_at',
        'modified_at',
        'status',
    )
    list_filter = (
        'vote',
        'vote_office',
        'observer',
        'created_at',
        'modified_at',
        'status',
        'id',
        'reference',
        'vote',
        'vote_office',
        'observer',
        'subscribed_number',
        'voters_number',
        'spoiled_ballots',
        'abstention',
        'created_at',
        'modified_at',
        'status',
    )
    date_hierarchy = 'created_at'


class IncidentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'reference',
        'vote_office',
        'incident_type',
        'reported_by',
        'incident_hour',
        'created_at',
        'modified_at',
    )
    list_filter = (
        'vote_office',
        'incident_type',
        'reported_by',
        'created_at',
        'modified_at',
        'id',
        'reference',
        'vote_office',
        'incident_type',
        'reported_by',
        'incident_hour',
        'created_at',
        'modified_at',
    )
    date_hierarchy = 'created_at'


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.VoteType, VoteTypeAdmin)
_register(models.CandidateType, CandidateTypeAdmin)
_register(models.IncidentType, IncidentTypeAdmin)
_register(models.Vote, VoteAdmin)
_register(models.Candidate, CandidateAdmin)
_register(models.VoteOffice, VoteOfficeAdmin)
_register(models.Observer, ObserverAdmin)
_register(models.VoteResult, VoteResultAdmin)
_register(models.Incident, IncidentAdmin)
