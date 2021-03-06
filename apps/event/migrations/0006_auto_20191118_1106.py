# Generated by Django 2.2.4 on 2019-11-18 10:06

from django.db import migrations, models
import event.models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_event_illustration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='entry_type',
            field=models.CharField(choices=[('LIBRE', 'LIBRE'), ('SUR INVITATION', 'SUR INVITATION')], default='LIBRE', max_length=255),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(null=True, verbose_name='Date evenement'),
        ),
        migrations.AlterField(
            model_name='event',
            name='illustration',
            field=models.FileField(blank=True, null=True, upload_to=event.models.Event.event_directory_path),
        ),
    ]
