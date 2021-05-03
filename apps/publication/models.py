from django.db import models
from utils.refs import reference
# Create your models here.
from django.template.defaultfilters import truncatewords  # or truncatewords



class Category(models.Model):

    name = models.CharField(max_length=255,unique=True)
    code = models.CharField(max_length=255,unique=True,default=reference)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    status = models.BooleanField(('Status'),help_text="Category's status in the system", default=True)

    class Meta:
        verbose_name = "Catégorie de publication"
        verbose_name_plural= "Catégories de publication"

    def __str__(self):
        return "%s"%self.name


class Quizz(models.Model):

    reference = models.CharField(max_length=255,unique=True,default=reference)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    status = models.BooleanField(('Status'),help_text="Quizz's status in the system", default=True)

    class Meta:
        verbose_name = "Le quizz"
        verbose_name_plural= "Les Quizz"

    def __str__(self):
        return "%s"%self.name


class Questions(models.Model):



    reference = models.CharField(max_length=255,unique=True,default=reference)
    quizz = models.ForeignKey(Quizz, max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING,related_name='questions')
    question = models.TextField(max_length=255)
    wrong_answer1 = models.CharField("Première fausse reponse",max_length=255,default="")
    wrong_answer2 = models.CharField("Deuxième fausse reponse",max_length=255,default="")
    correct_answer = models.CharField("Bonne reponse",max_length=255,default="")
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    status = models.BooleanField(('Status'),help_text="Question's status in the system", default=True)

    class Meta:
        verbose_name = "Question quizz"
        verbose_name_plural= "Questions quizz"

    def __str__(self):
        return "%s"%self.question


class Publication(models.Model):

    def  publication_directory_path(self, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'publication_{0}/{1}'.format(self.reference, filename)


    reference = models.CharField(max_length=255,unique=True,default=reference)
    name = models.CharField("Titre",max_length=255)
    summary = models.TextField("Contenu",max_length=10000000000,null=True)
    content_img = models.FileField(upload_to=publication_directory_path,null=True,blank=True)
    content_video = models.CharField("Contenu video",max_length=255,null=True,blank=True)
    category = models.ForeignKey(Category,help_text=("Categorie"), max_length=128, null=True, blank=False,on_delete = models.DO_NOTHING)
    quizz = models.ForeignKey(Quizz, help_text=("Quizz"), max_length=128, null=True, blank=True ,on_delete = models.DO_NOTHING)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    status = models.BooleanField(('Status'),help_text="Publication's status in the system", default=True)
    add_to_slider = models.BooleanField(('Add to slider ?'),help_text="Add this publication to slider ", default=False)

    class Meta:
        verbose_name = "La publication"
        verbose_name_plural= "Les publications"

    def __str__(self):
        return "%s"%self.name


    @property
    def short_summary(self):
        return truncatewords(self.summary, 10)



    def json(self):

        return {
        "id" : self.id,
        "reference":self.reference,
        "name":self.name,
        "summary" : self.summary,
        "content_img" : "https://core.malicratie.com/media/"+self.content_img.name,
        "content_video" : self.content_video,
        "category" : self.category.name,
        "add_to_slider" : self.add_to_slider,
        "model" : Publication.__name__

        }
