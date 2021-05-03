from tastypie.resources import ModelResource
#from base.models import Partner, About, ProjectType, FundingType
from base.models import Partner, About
from tastypie import fields
from tastypie.resources import ALL_WITH_RELATIONS, ALL


class PartnersResource(ModelResource):
    class Meta:
        queryset = Partner.objects.all().order_by('-id')
        resource_name = 'partners'
        allowed_methods = ['get']

    def dehydrate_logo(self,bundle):
        logo = bundle.data['logo']
        return f"https://core.malicratie.com{logo}"


class AboutResource(ModelResource):
    class Meta:
        queryset = About.objects.filter(status=True)
        resource_name = 'aboutus'
        allowed_methods = ['get']


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
