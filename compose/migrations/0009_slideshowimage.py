# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0008_auto_20151026_1109'),
        ('compose', '0008_auto_20150916_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlideshowImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('order', models.IntegerField()),
                ('content', models.ForeignKey(to='compose.Slideshow')),
                ('image', models.ForeignKey(to='block.Image')),
            ],
            options={
                'verbose_name_plural': 'Slideshow Images',
                'verbose_name': 'Slideshow Image',
                'ordering': ['order'],
            },
        ),
    ]
