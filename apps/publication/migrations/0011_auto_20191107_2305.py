# Generated by Django 2.2.4 on 2019-11-07 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0010_auto_20191107_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='correct_answer',
            field=models.CharField(default='', max_length=255, verbose_name='Bonne reponse'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='wrong_answer1',
            field=models.CharField(default='', max_length=255, verbose_name='Première fausse reponse'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='wrong_answer2',
            field=models.CharField(default='', max_length=255, verbose_name='Deuxième fausse reponse'),
        ),
    ]