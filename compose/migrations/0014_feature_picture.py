# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0011_auto_20151030_1551'),
        ('compose', '0013_auto_20151105_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='picture',
            field=models.ForeignKey(blank=True, to='block.Image', related_name='feature_picture', null=True),
        ),
    ]
