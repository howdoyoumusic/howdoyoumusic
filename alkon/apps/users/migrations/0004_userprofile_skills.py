# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_cell_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='skills',
            field=models.ManyToManyField(to='users.Skills'),
        ),
    ]
