# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_skills_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cell_phone',
            field=models.IntegerField(default=11111111),
            preserve_default=False,
        ),
    ]
