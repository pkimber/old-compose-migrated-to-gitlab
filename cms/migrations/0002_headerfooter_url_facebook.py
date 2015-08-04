# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='headerfooter',
            name='url_facebook',
            field=models.URLField(verbose_name='Facebook URL', blank=True),
        ),
    ]
