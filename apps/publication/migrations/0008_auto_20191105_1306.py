# Generated by Django 2.2.4 on 2019-11-05 13:06

from django.db import migrations, models
import utils.refs


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0007_auto_20191103_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(default=utils.refs.reference, max_length=255, unique=True)),
                ('content', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modification date')),
                ('status', models.BooleanField(default=False, help_text='True if this is the right answer', verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
            },
        ),
        migrations.RemoveField(
            model_name='questions',
            name='answers',
        ),
        migrations.AddField(
            model_name='questions',
            name='answers',
            field=models.ManyToManyField(blank=True, max_length=128, null=True, to='publication.Answer'),
        ),
    ]