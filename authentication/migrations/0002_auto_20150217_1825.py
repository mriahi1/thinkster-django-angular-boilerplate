# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(unique=True, max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='account',
            name='tagline',
            field=models.CharField(max_length=140, blank=True),
            preserve_default=True,
        ),
    ]
