from tastypie.resources import ModelResource, Resource
from project.models import Project, Denonciation
from project.api.resources import ProjectResource
from tastypie import fields
from django.conf.urls import url
from tastypie.utils import trailing_slash
from django.http import HttpResponse
from tastypie.resources import ALL_WITH_RELATIONS, ALL
from geo.api.resources import GeoResource
from utils.exceptions import CustomBadRequest
from . import MultipartResource

from django.db.models import Q
import json



class DenonciationResource(MultipartResource,ModelResource):
    project = fields.ForeignKey(ProjectResource, attribute='project', null=True,full=True)
    geo_zone = fields.ToManyField(GeoResource, attribute='geo_zone', null=True,full=True)
    content_img = fields.FileField(attribute="content_img", null=True, blank=True)
    content_video = fields.FileField(attribute="content_video", null=True, blank=True)
    content_audio = fields.FileField(attribute="content_audio", null=True, blank=True)

    class Meta:
        queryset = Denonciation.objects.all().order_by('-id')
        resource_name = 'trackas'
        filtering = {
            'id': ALL,
            'project' : ALL_WITH_RELATIONS,
            'geo_zone' : ALL_WITH_RELATIONS,
        }


    def prepend_urls(self):
           return [
           url(r"^tracka/new%s$"  %(trailing_slash()), self.wrap_view('new_tracka'), name="api_new_tracka")

       ]

    def new_tracka(self ,request, **kwargs):
        data = self.deserialize(request, request.body)
        try:
            project_id = data['project_id']
            content = data['content']
            name = data['name']

            obj = Denonciation()
            obj.project = Project.objects.get(id=project_id)
            #TODO : Check the content type before recording the content
            
            obj.content_text = content
            if 'content_img' in request.FILES:
                obj.content_img = request.FILES['content_img']
            
            if 'content_video' in request.FILES:
                obj.content_video = request.FILES['content_video']
            
            if 'content_audio' in request.FILES:
                obj.content_audio = request.FILES['content_audio']

            obj.name = name
            obj.save()
            bundle = self.build_bundle(obj=obj, request=request)  # take queryset obj & request
            bundle = self.full_dehydrate(bundle)

        except Exception as e:
            print (e)
            raise CustomBadRequest("KO","Une erreur est survenue. Merci de reessayer plus tard.")

        return self.create_response(request, bundle)
