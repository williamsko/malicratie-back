# vim: set fileencoding=utf-8 :
from django.contrib import admin
from users.models import Profile
from django import forms

from . import models


class EventTypeAdmin(admin.ModelAdmin):

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


class EventAdminForm(forms.ModelForm):
    class Meta:
        model = models.Event
        exclude = ('status',) 

    def __init__(self, *args, **kwargs):
        super(EventAdminForm, self).__init__(*args, **kwargs)
        if self.instance and not self.current_user.is_superuser:
            profile = Profile.objects.get(user=self.current_user)
            self.fields['geo_zone'].queryset = profile.geo_zone


class EventAdmin(admin.ModelAdmin):

    form = EventAdminForm

    #def get_queryset(self, request):
    #    qs = super(EventAdmin, self).get_queryset(request)
    #    user = request.user
    #    if user.is_superuser:
    #        return qs
    #    profile = Profile.objects.get(user=user)
    #    return models.Event.objects.filter(geo_zone = profile.geo_zone)

    def get_form(self, request, obj=None, **kwargs):
        form = super(EventAdmin, self).get_form(request, obj, **kwargs)
        form.current_user = request.user
        return form

    list_display = (
        'entry_type',
        'type',
        'title',
        'adress',
        'short_summary',
        'event_date',
        'created_at',
        'modified_at',
        'status',
    )
    list_filter = (
        'type',
        'event_date',
        'created_at',
        'modified_at',
        'status',
        'id',
        'entry_type',
        'type',
        'status',
    )
    date_hierarchy = 'created_at'


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.EventType, EventTypeAdmin)
_register(models.Event, EventAdmin)
