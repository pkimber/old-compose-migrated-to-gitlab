# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def convert_slideshow(apps, schema_editor):
    slideshow_class = apps.get_model('compose', 'Slideshow')
    slideshow_image_class = apps.get_model('compose', 'SlideshowImage')
    for row in slideshow_class.objects.all():
        order = 0
        for obj in row.slideshow.all():
            order = order + 1
            instance = slideshow_image_class(**dict(
                content=row,
                image=obj,
                order=order,
            ))
            instance.save()
            instance.full_clean()


class Migration(migrations.Migration):

    dependencies = [
        ('compose', '0009_slideshowimage'),
    ]

    operations = [
        migrations.RunPython(convert_slideshow),
    ]
