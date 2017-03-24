# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='create time')),
                ('updated', models.DateTimeField(verbose_name='update time', auto_now=True)),
                ('deleted', models.DateTimeField(blank=True, default=None, verbose_name='delete time', null=True)),
                ('pinyin', models.CharField(blank=True, null=True, max_length=20)),
                ('in_use', models.NullBooleanField(default=True, verbose_name='in use')),
                ('remark', models.TextField(blank=True, verbose_name='remark', null=True)),
                ('mobile_phone', models.CharField(blank=True, unique=True, null=True, max_length=11)),
                ('landline', models.CharField(blank=True, verbose_name='landline', null=True, max_length=20)),
                ('used_email', models.EmailField(blank=True, null=True, max_length=254)),
                ('fax', models.CharField(blank=True, verbose_name='fax', null=True, max_length=30)),
                ('qq', models.CharField(blank=True, unique=True, null=True, max_length=13)),
                ('wx', models.CharField(blank=True, unique=True, null=True, max_length=20)),
                ('sina_weibo', models.CharField(blank=True, null=True, max_length=256)),
                ('alipay', models.CharField(blank=True, unique=True, null=True, max_length=256)),
                ('nationality', models.CharField(blank=True, null=True, max_length=30)),
                ('province', models.CharField(blank=True, null=True, max_length=30)),
                ('city', models.CharField(blank=True, null=True, max_length=30)),
                ('county', models.CharField(blank=True, null=True, max_length=30)),
                ('address', models.CharField(blank=True, null=True, max_length=220)),
                ('auth_user', models.OneToOneField(to=settings.AUTH_USER_MODEL, parent_link=True, serialize=False, primary_key=True)),
                ('nickname', models.CharField(blank=True, verbose_name='nickname', null=True, max_length=60)),
                ('name', models.CharField(blank=True, verbose_name='name', null=True, max_length=60)),
                ('age', models.IntegerField(blank=True, verbose_name='age', null=True)),
                ('sex', models.CharField(choices=[('0', 'male'), ('1', 'Female'), ('2', 'Not determined')], blank=True, verbose_name='sex', null=True, max_length=1)),
                ('gender', models.CharField(choices=[('0', 'male'), ('1', 'Female'), ('2', 'Not determined')], blank=True, verbose_name='gender', null=True, max_length=1)),
                ('birthday', models.DateField(blank=True, verbose_name='birthday', null=True)),
                ('id_card', models.CharField(blank=True, verbose_name='id_card', null=True, max_length=20)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, related_name='user_user_creator', null=True, verbose_name='creator')),
                ('updater', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, related_name='user_user_updater', null=True, verbose_name='updater')),
            ],
            options={
                'db_table': 'user',
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
            },
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
