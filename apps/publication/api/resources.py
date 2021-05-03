from tastypie.resources import ModelResource
from publication.models import Publication, Questions, Quizz, Category
from tastypie import fields
from tastypie.resources import ALL_WITH_RELATIONS, ALL






class QuestionsResource(ModelResource):

    class Meta:
        queryset = Questions.objects.all().order_by('-id')
        resource_name = 'questions'
        allowed_methods = ['get']

class CategoryResource(ModelResource):

    class Meta:
        queryset = Category.objects.all().order_by('-id')
        resource_name = 'categories'
        allowed_methods = ['get']

        filtering = {
            'id': ALL,
        }

class QuizzResource(ModelResource):
    questions = fields.ToManyField(QuestionsResource,'questions', null=True,full=True)

    class Meta:
        queryset = Quizz.objects.all().order_by('-id')
        resource_name = 'quizz'
        allowed_methods = ['get']

class PublicationsResource(ModelResource):
    quizz = fields.ForeignKey(QuizzResource, attribute='quizz', null=True,full=True)
    category = fields.ForeignKey(CategoryResource, attribute='category', null=True,full=True)

    def dehydrate_content_img(self,bundle):
        content_img = bundle.data['content_img']
        return f"https://core.malicratie.com{content_img}"

    class Meta:
        queryset = Publication.objects.all().order_by('-id')
        resource_name = 'publications'
        allowed_methods = ['get']
        filtering = {
            'id': ALL,
            'add_to_slider' : ALL,
            'category' : ALL_WITH_RELATIONS,
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
