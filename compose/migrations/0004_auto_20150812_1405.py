# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def move_picture(apps, schema_editor):
    """Move contents of 'picture_old' to the 'picture' image link."""
    article_model = apps.get_model('compose', 'Article')
    image_model = apps.get_model('block', 'Image')
    pks = [obj.pk for obj in article_model.objects.all()]
    for pk in pks:
        article = article_model.objects.get(pk=pk)
        # create an 'Image' instance
        image = image_model(**dict(
            title='Image Title',
            image=article.picture_old,
            original_file_name=os.path.basename(article.picture_old.name),
        ))

        image.save()
        article.picture = image
        article.save()


class Migration(migrations.Migration):

    dependencies = [
        ('compose', '0003_auto_20150812_1405'),
    ]

    operations = [
        migrations.RunPython(move_picture),
    ]
