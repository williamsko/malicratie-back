from django.db import models
#from base.models import ProjectType , FundingType
from geo.models import Geo
from utils.refs import reference
from django.template.defaultfilters import truncatewords  # or truncatewords

# Create your models here.


class EventType(models.Model):

    name = models.CharField(max_length=255,unique=True)
    code = models.CharField(max_length=255,unique=True,default=reference)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    status = models.BooleanField(('Status'),help_text="Event type's status in the system", default=True)

    class Meta:
        verbose_name = "Type d'évènement"
        verbose_name_plural= "Type d'évènements"

    def __str__(self):
        return "%s"%self.name

class Event(models.Model):

    def event_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'event_{0}/{1}'.format(instance.reference, filename)

    LIBRE  = 'LIBRE'
    PRIVE = 'SUR INVITATION'

    ENTRY_TYPE_CHOICES = [
        (LIBRE, 'LIBRE'),
        (PRIVE, 'SUR INVITATION'),
    ]

    entry_type = models.CharField(
        max_length=255,
        choices=ENTRY_TYPE_CHOICES,
        default=LIBRE,
    )
    reference = models.CharField(max_length=255,unique=True,default=reference)
    title = models.CharField(max_length=255)
    type = models.ForeignKey(EventType,help_text=("Type d'evènement"), max_length=128, null=True, blank=False,on_delete = models.DO_NOTHING)
    geo_zone = models.ForeignKey(Geo, max_length=128, null=True, blank=True,on_delete=models.DO_NOTHING)


    adress = models.CharField(max_length=255)
    summary = models.TextField(max_length=1000)
    event_date = models.DateTimeField(('Date evenement'),null=True )
    illustration = models.FileField(upload_to=event_directory_path,null=True,blank=True)

    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    status = models.BooleanField(('Status'),help_text="Event's status in the system", default=True)

    class Meta:
        verbose_name = "Evènement"
        verbose_name_plural= "Evènements"

    def __str__(self):
        return "%s"%self.title

    @property
    def short_summary(self):
        return truncatewords(self.summary, 10)


    def json(self):
        
        return {
        "id" : self.id,
        "reference":self.reference,
        "title":self.title,
        "adress" : self.adress,
        "summary" : self.summary,
        "event_date" : str(self.event_date),
        "model" : Event.__name__

        }
