# Generated by Django 2.2.4 on 2019-11-10 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='entry_type',
            field=models.CharField(choices=[('LIBRE', 'LIBRE'), ('PRIVE', 'PRIVE')], default='LIBRE', max_length=255),
        ),
    ]
