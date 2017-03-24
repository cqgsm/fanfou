# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='credit',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='popularity',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
