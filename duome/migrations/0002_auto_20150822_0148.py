# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('duome', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='nickname',
            field=models.CharField(max_length=64, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='ucode',
            field=models.IntegerField(default=0),
        ),
    ]
