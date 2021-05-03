# Generated by Django 2.2.4 on 2019-11-10 13:14

from django.db import migrations, models
import django.db.models.deletion
import utils.refs


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0003_auto_20191110_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdecs',
            name='budget',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Budget'),
        ),
        migrations.CreateModel(
            name='PDECSDetailedBudget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Label dépense')),
                ('reference', models.CharField(default=utils.refs.reference, max_length=255, unique=True)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Montant')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modification date')),
                ('pdecs', models.ForeignKey(help_text='PDECS Budget', max_length=128, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='geo.Geo')),
            ],
            options={
                'verbose_name': 'Budget détaillé',
                'verbose_name_plural': 'Budget détaillé',
            },
        ),
    ]