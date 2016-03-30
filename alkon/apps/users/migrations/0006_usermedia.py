# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20160329_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMedia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('media_type', models.PositiveSmallIntegerField(choices=[(0, 'Audio'), (1, 'Image'), (2, 'Video')])),
                ('media_url', models.FileField(upload_to='uploads')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
