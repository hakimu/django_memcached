# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('album_text', models.CharField(max_length=200)),
                ('company_text', models.CharField(max_length=200)),
                ('release_date', models.DateTimeField(verbose_name=b'date released')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('artist_text', models.CharField(max_length=200)),
                ('album', models.ForeignKey(to='records.Album')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
