from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from utils.refs import reference

# Create your models here.


class Geo(MPTTModel):
    COUNTRY = 'COUNTRY'
    CERCLE = 'CERCLE'
    REGION = 'REGION'
    ARRONDISSEMENT = 'ARRONDISSEMENT'
    COMMUNE = 'COMMUNE'

    GEO_TYPE_CHOICES = [
        (COUNTRY, 'COUNTRY'),
        (CERCLE, 'CERCLE'),
        (REGION, 'REGION'),
        (ARRONDISSEMENT, 'ARRONDISSEMENT'),
        (COMMUNE, 'COMMUNE'),
    ]

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, unique=True, default=reference)
    type = models.CharField(
        max_length=255,
        choices=GEO_TYPE_CHOICES,
        default=COUNTRY,
    )

    lon = models.CharField("Longitude", max_length=255, blank=True, null=True)
    lat = models.CharField("Latitude", max_length=255, blank=True, null=True)
    nb_hbts = models.CharField(
        "Nombre d'habitants", max_length=255, null=True, blank=True)
    area = models.CharField(
        "Superficie", max_length=255, blank=True, null=True)
    manager = models.CharField(
        "Manager", max_length=255, blank=True, null=True)

    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')
    created_at = models.DateTimeField(
        ('Creation date'), auto_now_add=True, null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)

    class Meta:
        verbose_name = "Découpage administratif "
        verbose_name_plural = "Découpages administratifs"

    def __str__(self):
        return "%s" % self.name

    def json(self):
        return {
            "id": self.id,
            "lon": self.lon,
            "lat": self.lat,
            "type": self.type,
            "nb_hbts": self.nb_hbts,
            "name": self.name,
            "manager": self.manager,
            "model": Geo.__name__,
            "parent": {
                "id": self.parent.id,
                "lon": self.parent.lon,
                "lat": self.parent.lat,
                "type": self.parent.type,
                "nb_hbts": self.parent.nb_hbts,
                "name": self.parent.name,
                "manager": self.parent.manager,

            }
        }


class PDECS(models.Model):

    def pdecs_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'project_{0}/{1}'.format(instance.reference, filename)

    name = models.CharField(max_length=255)
    reference = models.CharField(
        max_length=255, unique=True, default=reference)
    budget = models.DecimalField("Budget", max_digits=20, decimal_places=2)
    geo = models.ForeignKey(Geo, help_text=("Découpage administratif concerné"),
                            max_length=128, null=True, blank=False, on_delete=models.DO_NOTHING)
    fichier_pdsec = models.FileField(upload_to=pdecs_directory_path)
    created_at = models.DateTimeField(
        ('Creation date'), auto_now_add=True, null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)

    class Meta:
        verbose_name = "Programme de développement économique, social et culturel "
        verbose_name_plural = "Programme de développement économique, social et culturel "

    def __str__(self):
        return "%s" % self.name


class PDECSDetailedBudget(models.Model):

    def pdecs_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'project_{0}/{1}'.format(instance.reference, filename)

    reference = models.CharField(
        max_length=255, unique=True, default=reference)
    sous_secteur = models.CharField("Sous secteur", max_length=25, null=True)
    objectifs = models.CharField("Objectifs", max_length=255, null=True)
    actions = models.CharField("Actions", max_length=255, null=True)
    year = models.CharField("Année", max_length=255, null=True)
    budget = models.IntegerField("Coût", max_length=20, blank=False)
    pdecs = models.ForeignKey(PDECS, help_text=(
        "PDECS Budget"), max_length=128, null=True, blank=False, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(
        ('Creation date'), auto_now_add=True, null=True, blank=True,)
    modified_at = models.DateTimeField('Modification date', auto_now=True)

    class Meta:
        verbose_name = "Budget détaillé"
        verbose_name_plural = "Budget détaillé"

    def __str__(self):
        return "%s" % self.reference
