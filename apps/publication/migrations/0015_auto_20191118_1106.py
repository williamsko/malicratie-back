# Generated by Django 2.2.4 on 2019-11-18 10:06

from django.db import migrations, models
import utils.refs


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0014_auto_20191110_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='code',
            field=models.CharField(default=utils.refs.reference, max_length=255, unique=True),
        ),
    ]
