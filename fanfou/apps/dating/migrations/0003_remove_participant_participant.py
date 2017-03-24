# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dating', '0002_auto_20170322_2323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='participant',
        ),
    ]
