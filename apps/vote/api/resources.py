from tastypie.resources import ModelResource
from vote.models import Vote, VoteOffice, Observer, Incident,IncidentType, VoteType
from tastypie import fields
from tastypie.resources import ALL_WITH_RELATIONS, ALL



class IncidentTypeResource(ModelResource):

    class Meta:
        queryset = IncidentType.objects.all().order_by('-id')
        resource_name = 'incident_type'
        allowed_methods = ['get']

class VoteTypeTypeResource(ModelResource):

    class Meta:
        queryset = VoteType.objects.all().order_by('-id')
        resource_name = 'vote_type'
        allowed_methods = ['get']

class VoteOfficeResource(ModelResource):

    class Meta:
        queryset = VoteOffice.objects.all().order_by('-id')
        resource_name = 'voteoffice'
        allowed_methods = ['get']



class VoteResource(MultipartResource,ModelResource):
   
    class Meta:
        queryset = Vote.objects.all().order_by('-id')
        resource_name = 'votes'  
        filtering = {
            'id': ALL,
        }


    def prepend_urls(self):
           return [
           url(r"^vote/new/result%s$"  %(trailing_slash()), self.wrap_view('new_result'), name="api_new_result"),
           url(r"^vote/new/incident%s$"  %(trailing_slash()), self.wrap_view('new_incident'), name="api_new_new_incident")

       ]

    def new_result(self ,request, **kwargs):
        
        data = self.deserialize(request, request.body)
        print (request.FILES) 
        try:
            vote_office = data['vote_office']
            subscribed_number = data['subscribed_number']
            spoiled_ballots = data['spoiled_ballots']
            abstention = data['abstention']
            voters_number = data['voters_number']

            obj = VoteResult()
            obj.save()
            bundle = self.build_bundle(obj=obj, request=request)  # take queryset obj & request
            bundle = self.full_dehydrate(bundle)

        except Exception as e:
            print (e)
            raise CustomBadRequest("KO","Une erreur est survenue. Merci de reessayer plus tard.")

        return self.create_response(request, bundle)

    
     def new_incident(self ,request, **kwargs):
        
        data = self.deserialize(request, request.body)
        print (request.FILES) 
        try:
            vote_office = data['vote_office']
            subscribed_number = data['subscribed_number']
            spoiled_ballots = data['spoiled_ballots']
            abstention = data['abstention']
            voters_number = data['voters_number']

            obj = VoteResult()
            obj.save()
            bundle = self.build_bundle(obj=obj, request=request)  # take queryset obj & request
            bundle = self.full_dehydrate(bundle)

        except Exception as e:
            print (e)
            raise CustomBadRequest("KO","Une erreur est survenue. Merci de reessayer plus tard.")

        return self.create_response(request, bundle)