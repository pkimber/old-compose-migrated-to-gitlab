# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compose', '0010_auto_20151026_1126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slideshow',
            old_name='slideshow',
            new_name='temp_slideshow',
        ),
    ]
