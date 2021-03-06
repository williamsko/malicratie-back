# Generated by Django 2.2.4 on 2019-11-10 12:43

from django.db import migrations, models
import django.db.models.deletion
import geo.models
import utils.refs


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDECS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('reference', models.CharField(default=utils.refs.reference, max_length=255, unique=True)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Budget détaillé')),
                ('fichier_pdsec', models.FileField(upload_to=geo.models.PDECS.pdecs_directory_path)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modification date')),
                ('geo', models.ForeignKey(help_text='Découpage administratif concerné', max_length=128, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='geo.Geo')),
            ],
            options={
                'verbose_name': 'Programme de développement économique, social et culturel ',
                'verbose_name_plural': 'Programme de développement économique, social et culturel ',
            },
        ),
    ]
