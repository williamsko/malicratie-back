from django.db import models
from utils.refs import reference

# Create your models here.





class Partner(models.Model):

    def partner_logo_path(self, filename):
        return 'partner_{0}/{1}'.format(self.brand_name.lower().replace(" ","-"),filename)

    brand_name = models.CharField(max_length=255)
    logo = models.FileField(upload_to=partner_logo_path)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    status = models.BooleanField(('Status'),help_text="Partner's status in the system", default=True)

    class Meta:
        verbose_name = "Partenaire Ajcad"
        verbose_name_plural= "Partenaires Ajcad"

    def __str__(self):
        return "%s"%self.brand_name


class About(models.Model):


    about = models.TextField(max_length=10000)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    status = models.BooleanField(('Status'),help_text="About's status in the system", default=True)

    class Meta:
        verbose_name = "Description AJCAD"
        verbose_name_plural= "Description AJCAD"

    def __str__(self):
        return "%s"%self.id
