from django.db import models
#from base.models import ProjectType , FundingType
from geo.models import Geo
from utils.refs import reference, reference_
from users.models import Profile
from django.template.defaultfilters import truncatewords  # or truncatewords

# Create your models here.


class ProjectType(models.Model):

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255,unique=True,default=reference)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    status = models.BooleanField(('Status'),help_text="Project's type  status in the system", default=True)

    class Meta:
        verbose_name = "Type de projet"
        verbose_name_plural= "Types de projets"

    def __str__(self):
        return "%s"%self.name


class FundingType(models.Model):    

    name = models.CharField(max_length=255,unique=True)
    code = models.CharField(max_length=255,unique=True,default=reference)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    status = models.BooleanField(('Status'),help_text="Funding's type  status in the system", default=True)

    class Meta:
        verbose_name = "Type d'investissement"
        verbose_name_plural= "Types d'investissements"

    def __str__(self):
        return "%s"%self.name



class ContractedEntreprise(models.Model):



    reference = models.CharField(max_length=255,unique=True,default=reference)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)

    class Meta:
        verbose_name = "Prestataires"
        verbose_name_plural= "Prestataires"

    def __str__(self):
        return "%s"%self.name



class Project(models.Model):

    def project_directory_path(self, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'project_{0}/{1}'.format(self.reference, filename)



    reference = models.CharField(max_length=255,unique=True,default=reference)
    name = models.CharField(max_length=255)
    type = models.ForeignKey(ProjectType, max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    contracted_entreprise = models.ForeignKey('ContractedEntreprise', max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    summary = models.TextField(max_length=10000000000)
    geo_zone = models.ManyToManyField(Geo, max_length=128, null=True, blank=True,related_name='projects')
    budget = models.IntegerField(max_length=20,blank=True,null=True)
    investor = models.CharField(max_length=255,blank=True,null=True)
    manager = models.CharField(max_length=255,blank=True,null=True)
    investment_type = models.ForeignKey(FundingType, max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    illustration = models.FileField(upload_to=project_directory_path)
    start_date = models.DateTimeField(('Starting date'),auto_now_add=True,null=True, blank=True,)
    duration = models.IntegerField(default=1)
    late_delay = models.IntegerField("Retard sur le projet en mois",default=0)
    evolution = models.IntegerField(default=1)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    status = models.BooleanField(('Status'),help_text="Quizz's status in the system", default=True)

    class Meta:
        verbose_name = "Projet"
        verbose_name_plural= "Projets"

    def __str__(self):
        return "%s"%self.name

    @property
    def short_summary(self):
        return truncatewords(self.summary, 10)

    @property
    def project_type_name(self):
        if self.type is None:
            return ""
        return self.type.name

    @property
    def project_investment_type_name(self):
        if self.investment_type is None:
            return ""
        return self.investment_type.name



    def json(self):
        
        return {
        "id" : self.id,
        "reference":self.reference,
        "name":self.name,
        "type" : self.project_type_name,
        "summary" : self.summary,
        "budget" : int(self.budget),
        "investor" : self.investor,
        "manager" : self.manager,
        "investment_type" : self.project_investment_type_name,
        "illustration" : "https://core.malicratie.com/media/"+self.illustration.name,
        "duration" : self.duration,
        "evolution" : self.evolution,
        "model" : Project.__name__

        }


class Comments(models.Model):

    def  comment_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'comment_{0}/{1}'.format(instance.reference, filename)

    reference = models.CharField(max_length=255,unique=True,default=reference)
    name = models.CharField(max_length=255,null=True,blank=True)
    project = models.ForeignKey(Project, max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    profile = models.ForeignKey(Profile, max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)

    TEXT  = 'TEXT'
    IMAGE = 'IMAGE'
    VIDEO = 'VIDEO'
    AUDIO = 'AUDIO'

    COMMENTS_CHOICES = [
        (TEXT, 'TEXT'),
        (IMAGE, 'IMAGE'),
        (VIDEO, 'VIDEO'),
    ]

    type = models.CharField(
        max_length=255,
        choices=COMMENTS_CHOICES,
        default=TEXT,
    )



    content_text = models.CharField(max_length=255,null=True,blank=True)
    content_img = models.FileField(upload_to=comment_directory_path,null=True,blank=True)
    content_video = models.FileField(upload_to=comment_directory_path,null=True,blank=True)
    content_audio = models.FileField(upload_to=comment_directory_path,null=True,blank=True)


    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    status = models.BooleanField(('Status'),help_text="Statut", default=True)

    class Meta:
        verbose_name = "Commentaire"
        verbose_name_plural= "Commentaires"

    def __str__(self):
        return "%s"%self.reference


class Denonciation(models.Model):

    def tracka_directory_path(self,instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'tracka_{0}/{1}'.format(instance.pk, filename)
    
    project = models.ForeignKey(Project, max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    name = models.CharField(max_length=255,null=True,blank=True)

    TEXT  = 'TEXT'
    IMAGE = 'IMAGE'
    VIDEO = 'VIDEO'
    AUDIO = 'AUDIO'

    COMMENTS_CHOICES = [
        (TEXT, 'TEXT'),
        (IMAGE, 'IMAGE'),
        (VIDEO, 'VIDEO'),
    ]

    type = models.CharField(
        max_length=255,
        choices=COMMENTS_CHOICES,
        default=TEXT,
    )

    geo_zone = models.ManyToManyField(Geo, max_length=128, null=True, blank=True,related_name="trackas")



    content_text = models.CharField(max_length=255,blank=True,null=True)
    content_img = models.FileField(upload_to=tracka_directory_path,null=True,blank=True)
    content_video = models.FileField(upload_to=tracka_directory_path,null=True,blank=True)
    content_audio = models.FileField(upload_to=tracka_directory_path,null=True,blank=True)


    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    status = models.BooleanField(('Information vérifiée'),help_text="Information vérifiée", default=False)

    class Meta:
        verbose_name = "Denonciation / Tracka"
        verbose_name_plural= "Denonciations / Trackas"

    def __str__(self):
        return "%s"%self.pk
