# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0008_auto_20151026_1109'),
        ('compose', '0011_auto_20151026_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slideshow',
            name='temp_slideshow',
        ),
        migrations.AddField(
            model_name='slideshow',
            name='slideshow',
            field=models.ManyToManyField(related_name='slideshow', to='block.Image', through='compose.SlideshowImage'),
        ),
    ]
