from tastypie.resources import ModelResource, Resource
from event.models import Event, EventType
from tastypie import fields
from django.conf.urls import url
from tastypie.utils import trailing_slash
from django.http import HttpResponse
from tastypie.resources import ALL_WITH_RELATIONS, ALL
from utils.exceptions import CustomBadRequest



class EventTypeResource(ModelResource):

    class Meta:
        queryset = EventType.objects.all().order_by('-id')
        resource_name = 'type'
        allowed_methods = ['get']


class EventResource(ModelResource):
    type = fields.ForeignKey(EventTypeResource, attribute='type', null=True,full=True)
    class Meta:
        queryset = Event.objects.all().order_by('event_date')
        resource_name = 'events'
        allowed_methods = ['get']

