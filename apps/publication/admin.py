# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CategoryAdmin(admin.ModelAdmin):

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


class QuizzAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'reference',
        'name',
        'created_at',
        'modified_at',
        'status',
    )
    list_filter = (
        'created_at',
        'modified_at',
        'status',
        'id',
        'reference',
        'name',
        'created_at',
        'modified_at',
        'status',
    )
    search_fields = ('name',)
    date_hierarchy = 'created_at'


class QuestionsAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'reference',
        'quizz',
        'question',
        'wrong_answer1',
        'wrong_answer2',
        'correct_answer',
        'created_at',
        'modified_at',
        'status',
    )
    list_filter = (
        'quizz',
        'created_at',
        'modified_at',
        'status',
        'id',
        'reference',
        'quizz',
        'question',
        'wrong_answer1',
        'wrong_answer2',
        'correct_answer',
        'created_at',
        'modified_at',
        'status',
    )
    date_hierarchy = 'created_at'


class PublicationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'reference',
        'name',
        'short_summary',
        'content_img',
        'content_video',
        'category',
        'quizz',
        'status',
        'add_to_slider',
    )
    list_filter = (
        'category',
        'created_at',
        'modified_at',
        'status',
        'add_to_slider',
    )
    search_fields = ('name',)
    date_hierarchy = 'created_at'


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Category, CategoryAdmin)
_register(models.Quizz, QuizzAdmin)
_register(models.Questions, QuestionsAdmin)
_register(models.Publication, PublicationAdmin)
