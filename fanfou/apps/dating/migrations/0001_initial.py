# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(verbose_name='create time', auto_now_add=True)),
                ('updated', models.DateTimeField(verbose_name='update time', auto_now=True)),
                ('deleted', models.DateTimeField(default=None, verbose_name='delete time', blank=True, null=True)),
                ('pinyin', models.CharField(max_length=20, blank=True, null=True)),
                ('in_use', models.NullBooleanField(default=True, verbose_name='in use')),
                ('remark', models.TextField(verbose_name='remark', blank=True, null=True)),
                ('title', models.CharField(verbose_name='title', max_length=30)),
                ('description', models.CharField(verbose_name='description', blank=True, max_length=120, null=True)),
                ('location', models.CharField(verbose_name='location', max_length=20)),
                ('dating_time', models.DateTimeField(verbose_name='dating time')),
                ('pay_method', models.IntegerField(verbose_name='pay method', choices=[(0, '女方付款'), (1, '女方付款'), (2, 'AA')])),
                ('pictures', models.TextField(verbose_name='pictures', blank=True, null=True)),
                ('status', models.IntegerField(default=0, verbose_name='status', choices=[(0, 'start'), (1, 'meet'), (2, 'end')])),
                ('creator', models.ForeignKey(related_name='dating_dating_creator', verbose_name='creator', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('updater', models.ForeignKey(related_name='dating_dating_updater', verbose_name='updater', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name_plural': 'dating',
                'verbose_name': 'dating',
                'db_table': 'dating',
            },
        ),
    ]
