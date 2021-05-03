from tastypie.resources import ModelResource, Resource
from project.models import Project, Comments
from project.api.resources import ProjectResource
from tastypie import fields
from django.conf.urls import url
from tastypie.utils import trailing_slash
from django.http import HttpResponse
from tastypie.resources import ALL_WITH_RELATIONS, ALL
from geo.api.resources import GeoResource
from utils.exceptions import CustomBadRequest
from django.db.models import Q
from utils.upload import handle_uploaded_file
import json
from . import MultipartResource




class CommentsResource(MultipartResource,ModelResource):
    project = fields.ForeignKey(ProjectResource, attribute='project', null=True,full=True)
    content_img = fields.FileField(attribute="content_img", null=True, blank=True)
    content_video = fields.FileField(attribute="content_video", null=True, blank=True)
    content_audio = fields.FileField(attribute="content_audio", null=True, blank=True)

    class Meta:
        queryset = Comments.objects.all().order_by('-id')
        resource_name = 'comments'  
        filtering = {
            'id': ALL,
            'project' : ALL_WITH_RELATIONS,
        }


    def prepend_urls(self):
           return [
           url(r"^comment/new%s$"  %(trailing_slash()), self.wrap_view('new_comment'), name="api_new_comment")

       ]

    def new_comment(self ,request, **kwargs):
        
        data = self.deserialize(request, request.body)
        print (request.FILES) 
        try:
            project_id = data['project_id']
            content = data['content']
            name = data['name']

            obj = Comments()
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


