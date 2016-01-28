# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models



def convert_feature(apps, schema_editor):
    image_class = apps.get_model('block', 'Image')
    feature_class = apps.get_model('compose', 'Feature')
    pks = []
    for row in feature_class.objects.all():
        pks.append(row.pk)
    for pk in pks:
        obj = feature_class.objects.get(pk=pk)
        if row.old_picture:
            image = image_class(
                title='Feature Image',
                image=row.old_picture,
            )
            image.save()
            obj.picture = image
            obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('compose', '0014_feature_picture'),
    ]

    operations = [
        migrations.RunPython(convert_feature),
    ]
