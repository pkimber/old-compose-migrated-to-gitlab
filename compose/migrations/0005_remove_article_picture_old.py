# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compose', '0004_auto_20150812_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='picture_old',
        ),
    ]
