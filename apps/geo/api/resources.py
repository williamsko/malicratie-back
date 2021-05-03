from tastypie.resources import ModelResource
from geo.models import Geo, PDECS
from tastypie.resources import  ALL, ALL_WITH_RELATIONS
from tastypie import fields


class GeoResource(ModelResource):
    class Meta:
        queryset = Geo.objects.all()
        allowed_methods = ['get']
        resource_name = 'geozone'

        filtering = {
            'id': ALL,
        }


class PDECSResource(ModelResource):
    geo_zone = fields.ForeignKey(GeoResource, attribute='geo_zone', null=True,full=True)

    class Meta:
        queryset = PDECS.objects.all().order_by('-id')
        resource_name = 'PDECS'
        filtering = {
            'id': ALL,
            'geo_zone' : ALL_WITH_RELATIONS,
        }

#class EventResource(ModelResource):
#    organizer = fields.ForeignKey(OrganizerResource, attribute='organizer', null=True,full=True)
#    categories = fields.ToManyField(CategoryResource, attribute='categories', null=True,full=True)
#    programs = fields.ToManyField(EventProgramResource, attribute='programs', null=True,full=True)
#    event_constraints_values = fields.ToManyField(ConstraintsValueResource, attribute='event_constraints_values', null=True,full=True)
#    partners = fields.ToManyField(PartnerResource, attribute='partners', null=True,full=True)
#    #event_pictures = fields.ToManyField(EventPictures, attribute='event_pictures', null=True,full=True)
#
#    class Meta:
#        queryset = Event.objects.all()
#        resource_name = 'events'
#        name = 'events'
#        allowed_methods = ['get']
#        always_return_data = True