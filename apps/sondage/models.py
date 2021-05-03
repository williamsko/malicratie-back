from django.db import models
from utils.refs import reference
# Create your models here.
from django.template.defaultfilters import truncatewords  # or truncatewords



class Questions(models.Model):

    reference = models.CharField(max_length=255,unique=True,default=reference)
    question = models.TextField(max_length=255)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    status = models.BooleanField(('Status'),help_text="Question's status in the system", default=True)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural= "Questions"

    def __str__(self):
        return "%s"%self.question


class Campaign(models.Model):

    reference = models.CharField(max_length=255,unique=True,default=reference)
    name = models.CharField(max_length=255)
    campaign_date = models.DateTimeField(('Debut Campagne'),null=True, blank=True,)
    end_campaign = models.DateTimeField(('Fin Campagne'),null=True, blank=True,)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    questions = models.ManyToManyField(Questions, max_length=128, null=True, blank=True)
    status = models.BooleanField(('Status'),help_text="Quizz's status in the system", default=True)

    class Meta:
        verbose_name = "Campagne"
        verbose_name_plural= "Campagnes"

    def __str__(self):
        return "%s"%self.name
