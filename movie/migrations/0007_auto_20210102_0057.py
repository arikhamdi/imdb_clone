# Generated by Django 3.1.4 on 2021-01-01 23:57

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_auto_20210102_0050'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=False, max_length=250, populate_from='title', unique_for_date='created'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='actor',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, max_length=100, populate_from='name', unique_for_date='created'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
