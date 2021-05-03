from tastypie.resources import ModelResource, Resource
from project.models import Project, ContractedEntreprise, ProjectType, FundingType, Denonciation
from publication.models import Publication
from geo.models import Geo
from tastypie import fields
from django.conf.urls import url
from tastypie.utils import trailing_slash
from django.http import HttpResponse
from tastypie.resources import ALL_WITH_RELATIONS, ALL
from geo.api.resources import GeoResource
from utils.exceptions import CustomBadRequest
from event.models import Event
from django.db.models import Q
import json


class ProjectTypeResource(ModelResource):
    class Meta:
        queryset = ProjectType.objects.all()
        allowed_methods = ['get']


class FundingTypeResource(ModelResource):
    class Meta:
        queryset = FundingType.objects.all()
        allowed_methods = ['get']


class ContractedEntrepriseResource(ModelResource):
    class Meta:
        queryset = ContractedEntreprise.objects.all().order_by('-id')
        resource_name = 'contracted_entreprise'
        allowed_methods = ['get']


class ProjectResource(ModelResource):
    type = fields.ForeignKey(
        ProjectTypeResource, attribute='type', null=True, full=True)
    contracted_entreprise = fields.ForeignKey(
        ContractedEntreprise, attribute='contracted_entreprise', null=True, full=True)
    investment_type = fields.ForeignKey(
        ProjectTypeResource, attribute='investment_type', null=True, full=True)
    geo_zone = fields.ToManyField(
        GeoResource, attribute='geo_zone', null=True, full=True)

    def dehydrate_illustration(self, bundle):
        illustration = bundle.data['illustration']
        return f"https://core.malicratie.com{illustration}"

    class Meta:
        queryset = Project.objects.all().order_by('-id')
        resource_name = 'projects'
        allowed_methods = ['get']
        filtering = {
            'id': ALL,
            'geo_zone': ALL_WITH_RELATIONS,
        }


class SearchResource(Resource):

    class Meta:
        resource_name = 'search'
        allowed_methods = ['get']
        object_name = "search"
        include_resource_uri = False

    def prepend_urls(self):
        return [
            url(r"^search%s$" % (trailing_slash()),
                self.wrap_view('search'), name="api_search")

        ]

    def search(self, request, **kwargs):
        query = request.GET.get('query', None)
        if not query:
            raise CustomBadRequest("KO", "Missing query parameter")

        # Should use haystack to get a score and make just one query
        events = Event.objects.filter(Q(title__icontains=query) | Q(
            adress__icontains=query) | Q(summary__icontains=query)).order_by('title')
        publications = Publication.objects.filter(
            Q(name__icontains=query) | Q(summary__icontains=query)).order_by('name')
        projects = Project.objects.filter(Q(name__icontains=query) | Q(
            geo_zone__name__icontains=query) | Q(summary__icontains=query)).order_by('name')
        zones = Geo.objects.filter(Q(name__icontains=query)).order_by('name')

        # Sort the merged list alphabetically and just return the top 20
        _projects = [obj.json() for obj in projects]
        _events = [obj.json() for obj in events]
        _publications = [obj.json() for obj in publications]
        _zones = [obj.json() for obj in zones]

        # return sorted(chain(_events,_publications,_projects))
        return HttpResponse(json.dumps({"data": _projects+_events+_publications+_zones}), content_type='application/json', status=200)


class GeoResource(ModelResource):
    projects = fields.ToManyField(
        ProjectResource, 'projects', related_name='projects', null=True, full=True)
    trackas = fields.ToManyField(
        'project.api.denonciation.DenonciationResource', 'trackas', related_name='trackas', null=True, full=True)
    pdecs = fields.ToManyField(
        'geo.api.resources.PDECSResource', 'pdecs_set', related_name='pdecs', blank=True, null=True, full=True)

    class Meta:
        queryset = Geo.objects.all().select_related('parent')
        allowed_methods = ['get']
        resource_name = 'geo'
        filtering = {
            'id': ALL,
            'type' : ALL,
        }

    def get_child_data(self, obj):
        data =  {
            'id': obj.id,
            'name': obj.name,
            'type': obj.type,
        }
        if not obj.is_leaf_node():
            data['children'] = [self.get_child_data(child) \
                                for child in obj.get_descendants()]
        return data

    
    def get_list(self, request, **kwargs):

        base_bundle = self.build_bundle(request=request)
        objects = self.obj_get_list(bundle=base_bundle, 
                                    **self.remove_api_resource_names(kwargs))
        sorted_objects = self.apply_sorting(objects, options=request.GET)

        paginator = self._meta.paginator_class(
            request.GET, sorted_objects, 
            resource_uri=self.get_resource_uri(), limit=self._meta.limit, 
            max_limit=self._meta.max_limit, 
            collection_name=self._meta.collection_name
        )
        to_be_serialized = paginator.page()

        from mptt.templatetags.mptt_tags import cache_tree_children
        objects = cache_tree_children(objects)

        bundles = []

        for obj in objects:
            data = self.get_child_data(obj)
            bundle = self.build_bundle(data=data, obj=obj, request=request)
            bundles.append(self.full_dehydrate(bundle))

        to_be_serialized[self._meta.collection_name] = bundles
        to_be_serialized = self.alter_list_data_to_serialize(request, 
                                                            to_be_serialized)
        return self.create_response(request, to_be_serialized)



# class EventResource(ModelResource):
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
