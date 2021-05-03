from django.db import models
from utils.refs import reference
from django.template.defaultfilters import truncatewords  # or truncatewords

# Create your models here.


class Parametrage(models.Model):

    ip_adress = models.CharField("Adresse IP", max_length=255,null=True)
    operateur = models.CharField("Opérateur", max_length=255,null=True)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)

    class Meta:
        verbose_name = "Paramétrage"
        verbose_name_plural= "Paramétrages"

    def __str__(self):
        return "%s"%self.operateur


class Operateur(models.Model):

    reference = models.CharField(max_length=255,unique=True,default=reference)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)
    status = models.BooleanField(('Status'),help_text="Staut opérateur", default=True)

    class Meta:
        verbose_name = "Operateur"
        verbose_name_plural= "Operateurs"

    def __str__(self):
        return "%s"%self.name



class SmsResponseParameter(models.Model):

    name = models.CharField("Code",max_length=255,null=True)
    meaning = models.CharField(max_length=255)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)

    class Meta:
        verbose_name = "Sms Response Parameter"
        verbose_name_plural= "Sms Response Parameter"

    def __str__(self):
        return "%s"%self.name

class SmsReceived(models.Model):

    number = models.CharField("Numero",max_length=255,null=True)
    sms_content = models.CharField("Contenu SMS",max_length=255)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)

    class Meta:
        verbose_name = "Sms Received"
        verbose_name_plural= "Sms Received"

    def __str__(self):
        return "%s"%self.number


class UssdRequest(models.Model):

    name = models.CharField("Code",max_length=255,null=True)
    meaning = models.CharField(max_length=255)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)

    class Meta:
        verbose_name = "Sms Response Parameter"
        verbose_name_plural= "Sms Response Parameter"

    def __str__(self):
        return "%s"%self.name


class UssdResponseParameter(models.Model):

    name = models.CharField("Code",max_length=255,null=True)
    response = models.CharField("Response", max_length=255)
    created_at = models.DateTimeField(('Creation date'),auto_now_add=True,null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)

    class Meta:
        verbose_name = "Ussd Response Parameter"
        verbose_name_plural= "Ussd Response Parameter"

    def __str__(self):
        return "%s"%self.name
