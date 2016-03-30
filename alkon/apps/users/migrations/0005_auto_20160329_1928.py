# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_userprofile_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cell_phone',
            field=models.BigIntegerField(),
        ),
    ]
