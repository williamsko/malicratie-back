# vim: set fileencoding=utf-8 :
from django.contrib import admin
from geo.models import Geo
from users.models import Profile
from django import forms
from . import models
from django.utils.html import mark_safe



class ProjectTypeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'code',
        'created_at',
        'modified_at',
        'status',
    )
    list_filter = (
        'created_at',
        'modified_at',
        'status',
        'id',
        'name',
        'code',
        'created_at',
        'modified_at',
        'status',
    )
    search_fields = ('name',)
    date_hierarchy = 'created_at'


class FundingTypeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'code',
        'created_at',
        'modified_at',
        'status',
    )
    list_filter = (
        'created_at',
        'modified_at',
        'status',
        'id',
        'name',
        'code',
        'created_at',
        'modified_at',
        'status',
    )
    search_fields = ('name',)
    date_hierarchy = 'created_at'


class ContractedEntrepriseAdmin(admin.ModelAdmin):

    list_display = ('id', 'reference', 'name', 'created_at', 'modified_at')
    list_filter = (
        'created_at',
        'modified_at',
        'id',
        'reference',
        'name',
        'created_at',
        'modified_at',
    )
    search_fields = ('name',)
    date_hierarchy = 'created_at'


class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = models.Project
        exclude = ('contracted_entreprise',) 

    def __init__(self, *args, **kwargs):
        super(ProjectAdminForm, self).__init__(*args, **kwargs)
        if self.instance and not self.current_user.is_superuser:
            profile = Profile.objects.get(user=self.current_user)
            self.fields['geo_zone'].queryset = profile.geo_zone


class ProjectAdmin(admin.ModelAdmin):

    form = ProjectAdminForm

    list_display = (
        'id',
        'reference',
        'name',
        'contracted_entreprise',
        'short_summary',
        'budget',
        'investor',
        'manager',
        'illustration',
        'start_date',
        'duration',
        'late_delay',
        'evolution',
        'created_at',
        'modified_at',
        'status',
    )
    list_filter = (
        'contracted_entreprise',
        'start_date',
        'created_at',
        'modified_at',
        'status',
        'id',
        'reference',
        'name',
        'contracted_entreprise',
        'budget',
        'manager',
        'illustration',
        'start_date',
        'duration',
        'late_delay',
        'evolution',
        'created_at',
        'modified_at',
        'status',
    )
    search_fields = ('name',)
    date_hierarchy = 'created_at'
    filter_horizontal = ('geo_zone',)

    def get_form(self, request, obj=None, **kwargs):
        form = super(ProjectAdmin, self).get_form(request, obj, **kwargs)
        form.current_user = request.user
        return form

    


class CommentsAdmin(admin.ModelAdmin):

    

    list_display = (
        'id',
        'project',
        'profile',
        'type',
        'content_text',
        'content_img',
        'content_video',
        'content_audio',
        'created_at',
        'modified_at',
        'status',
    )
    list_filter = (
       
        'status',
    )
    date_hierarchy = 'created_at'

  


class DenonciationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'project',
        'type',
        'content_text',
        'content_img',
        'content_video',
        'content_audio',
        'created_at',
        'modified_at',
        'status',
    )
    list_filter = (
        'project',
        'created_at',
        'modified_at',
        'status',
        'id',
        'project',
        'type',
        'content_text',
        'content_img',
        'content_video',
        'content_audio',
        'created_at',
        'modified_at',
        'status',
    )
    filter_horizontal = ('geo_zone',)
    date_hierarchy = 'created_at'


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.ProjectType, ProjectTypeAdmin)
_register(models.FundingType, FundingTypeAdmin)
_register(models.ContractedEntreprise, ContractedEntrepriseAdmin)
_register(models.Project, ProjectAdmin)
_register(models.Comments, CommentsAdmin)
_register(models.Denonciation, DenonciationAdmin)
