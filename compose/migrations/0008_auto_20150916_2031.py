# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compose', '0007_codesnippet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='slideshow',
            name='title',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
