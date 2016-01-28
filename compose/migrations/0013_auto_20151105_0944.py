# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compose', '0012_auto_20151026_1203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feature',
            old_name='picture',
            new_name='old_picture',
        ),
    ]
