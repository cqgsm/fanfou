# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dating', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='create time')),
                ('updated', models.DateTimeField(verbose_name='update time', auto_now=True)),
                ('deleted', models.DateTimeField(null=True, verbose_name='delete time', default=None, blank=True)),
                ('pinyin', models.CharField(null=True, max_length=20, blank=True)),
                ('in_use', models.NullBooleanField(verbose_name='in use', default=True)),
                ('remark', models.TextField(null=True, verbose_name='remark', blank=True)),
                ('agree', models.NullBooleanField()),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='creator', null=True, related_name='dating_participant_creator', blank=True)),
            ],
            options={
                'verbose_name': 'Participant',
                'verbose_name_plural': 'Participant',
            },
        ),
        migrations.AlterField(
            model_name='dating',
            name='pay_method',
            field=models.IntegerField(choices=[(0, '女方付款'), (1, '男方付款'), (2, 'AA')], verbose_name='pay method'),
        ),
        migrations.AlterField(
            model_name='dating',
            name='status',
            field=models.IntegerField(choices=[(0, 'start'), (1, 'meet'), (2, 'end'), (3, 'cancel')], default=0, verbose_name='status'),
        ),
        migrations.AddField(
            model_name='participant',
            name='dating',
            field=models.ForeignKey(to='dating.Dating'),
        ),
        migrations.AddField(
            model_name='participant',
            name='participant',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='participant',
            name='updater',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='updater', null=True, related_name='dating_participant_updater', blank=True),
        ),
    ]
