# Generated by Django 2.2.4 on 2019-11-01 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_event_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='late_delay',
            field=models.IntegerField(default=0, verbose_name='Retard sur le projet en mois'),
        ),
    ]
