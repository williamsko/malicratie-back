# Generated by Django 2.2.4 on 2019-10-31 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='summary',
            field=models.TextField(max_length=10000000000, null=True, verbose_name='Contenu'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='category',
            field=models.ForeignKey(help_text='Categorie', max_length=128, on_delete=django.db.models.deletion.DO_NOTHING, to='base.Category'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Titre'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='quizz',
            field=models.ForeignKey(help_text='Quizz', max_length=128, on_delete=django.db.models.deletion.DO_NOTHING, to='publication.Quizz'),
        ),
    ]
