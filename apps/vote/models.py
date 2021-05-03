from django.db import models
from geo.models import Geo
from utils.refs import reference, reference_
from users.models import Profile
from django.template.defaultfilters import truncatewords  # or truncatewords

# Create your models here.


class VoteType(models.Model):

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255,unique=True,default=reference)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    status = models.BooleanField(('Status'),help_text="status in the system", default=True)

    class Meta:
        verbose_name = "Type de scrutin"
        verbose_name_plural= "Types de scrutin"

    def __str__(self):
        return "%s"%self.name


class CandidateType(models.Model):

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255,unique=True,default=reference)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    status = models.BooleanField(('Status'),help_text="Status in the system", default=True)

    class Meta:
        verbose_name = "Tyoe de candidat"
        verbose_name_plural= "Types de canditatss"

    def __str__(self):
        return "%s"%self.name


class IncidentType(models.Model):

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255,unique=True,default=reference)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    status = models.BooleanField(('Status'),help_text="status in the system", default=True)

    class Meta:
        verbose_name = "Type d'incident"
        verbose_name_plural= "Types d'incident"

    def __str__(self):
        return "%s"%self.name

class Vote(models.Model):


    reference = models.CharField(max_length=255,unique=True,default=reference)
    name = models.CharField(max_length=255)
    type = models.ForeignKey(VoteType, max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    vote_date = models.DateTimeField(('Starting date'),auto_now_add=True,null=True, blank=True,)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    status = models.BooleanField(('Status'),help_text="Vote's status in the system", default=True)

    class Meta:
        verbose_name = "Scrutin"
        verbose_name_plural= "Scrutin"

    def __str__(self):
        return "%s"%self.name



class Candidate(models.Model):

    def  candidate_directory_path(self,instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'candidate_{0}/{1}'.format(instance.reference, filename)


    reference = models.CharField(max_length=255,unique=True,default=reference)
    name = models.CharField(max_length=255)
    type = models.ForeignKey(CandidateType, max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    parti = models.CharField(max_length=255,null=True,blank=True)
    photo = models.FileField(upload_to=candidate_directory_path,null=True,blank=True)
    color = models.CharField(max_length=255,null=True,blank=True)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    status = models.BooleanField(('Status'),help_text="Candidate's status in the system", default=True)

    class Meta:
        verbose_name = "Candidat"
        verbose_name_plural= "Candidats"

    def __str__(self):
        return "%s"%self.name


class VoteOffice(models.Model):


    reference = models.CharField(max_length=255,unique=True,default=reference)
    name = models.CharField(max_length=255)
    geo_zone = models.ForeignKey(Geo, max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    open_hour = models.TimeField(max_length=255,null=True,blank=True)
    close_hour = models.TimeField(max_length=255,null=True,blank=True)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    status = models.BooleanField(('Status'),help_text="VoteOffice's status in the system", default=True)

    class Meta:
        verbose_name = "Bureau de vote"
        verbose_name_plural= "Bureaux de vote"

    def __str__(self):
        return "%s"%self.name


class Observer(models.Model):

    def  observer_directory_path(self,instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'observer_{0}/{1}'.format(instance.reference, filename)


    reference = models.CharField(max_length=255,unique=True,default=reference)
    photo = models.FileField(upload_to=observer_directory_path,null=True,blank=True)
    profile = models.ForeignKey(Profile, max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    vote_office = models.ForeignKey(VoteOffice, max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    status = models.BooleanField(('Status'),help_text="Observer's status in the system", default=True)

    class Meta:
        verbose_name = "Observateur"
        verbose_name_plural= "Observateurs"

    def __str__(self):
        return "%s"%self.reference

class VoteResult(models.Model):

    reference = models.CharField(max_length=255,unique=True,default=reference)
    vote= models.ForeignKey(Vote, max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    vote_office = models.ForeignKey(VoteOffice, max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    observer = models.ForeignKey(Observer, max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    subscribed_number = models.BigIntegerField(null=True,blank=True)
    voters_number = models.BigIntegerField(null=True,blank=True)
    spoiled_ballots = models.BigIntegerField("Bulletins nuls",null=True,blank=True)
    abstention = models.BigIntegerField("Abstention",null=True,blank=True)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    status = models.BooleanField(('Status'),help_text="Candidate's status in the system", default=True)

    class Meta:
        verbose_name = "Résultat de vote"
        verbose_name_plural= "Résultats de vote"

    def __str__(self):
        return "%s"%self.reference


class Incident(models.Model):

    reference = models.CharField(max_length=255,unique=True,default=reference)
    vote_office = models.ForeignKey(VoteOffice, max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    incident_type = models.ForeignKey(IncidentType, max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    reported_by = models.ForeignKey(Observer, max_length=128, null=True, blank=True,on_delete = models.DO_NOTHING)
    incident_hour = models.TimeField() 
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)

    class Meta:
        verbose_name = "Incident"
        verbose_name_plural= "Incidents"

    def __str__(self):
        return "%s"%self.reference
