from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from geo.models import Geo

# Create your models here.


class Profile(models.Model):

    SIMPLE = 'SIMPLE'
    AGREED = 'AGREED'
    VISITOR = 'VISITOR'
    EDITOR = 'EDITOR'

    USER_TYPE_CHOICES = [
        (SIMPLE, 'SIMPLE'),
        (AGREED, 'AGREED'),
        (VISITOR, 'VISITOR'),
        (EDITOR, 'EDITOR'),
    ]


    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    type = models.CharField(
        max_length=255,
        choices=USER_TYPE_CHOICES,
        default=SIMPLE,
    )
    geo_zone = models.ManyToManyField(Geo, max_length=128, null=True, blank=True)



    class Meta:
        verbose_name = "Profile"
        verbose_name_plural= "Profiles"

    def __str__(self):
        return "%s"%self.user.username
