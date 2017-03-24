# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dating', '0004_auto_20170324_1547'),
        ('user', '0003_auto_20170323_0026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='create time')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='update time')),
                ('deleted', models.DateTimeField(null=True, blank=True, default=None, verbose_name='delete time')),
                ('pinyin', models.CharField(max_length=20, blank=True, null=True)),
                ('in_use', models.NullBooleanField(default=True, verbose_name='in use')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='remark')),
                ('impression', models.DecimalField(default=0, decimal_places=1, max_digits=3)),
                ('content', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Evaluation',
                'verbose_name': 'Evaluation',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=1, choices=[('0', 'Female'), ('1', 'male'), ('2', 'Not determined')], blank=True, null=True, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(max_length=1, choices=[('0', 'Female'), ('1', 'male'), ('2', 'Not determined')], blank=True, null=True, verbose_name='sex'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='creator', blank=True, related_name='user_evaluation_creator', null=True),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='related_dating',
            field=models.ForeignKey(to='dating.Dating', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='updater',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='updater', blank=True, related_name='user_evaluation_updater', null=True),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
