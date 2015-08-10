# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0004_auto_20150810_1526'),
        ('compose', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='picture',
        ),
        migrations.AddField(
            model_name='article',
            name='carousel',
            field=models.ManyToManyField(to='block.Image'),
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ForeignKey(blank=True, null=True, related_name='picture', to='block.Image'),
        ),
        migrations.AddField(
            model_name='article',
            name='image_size',
            field=models.CharField(max_length=3, default='1-2', choices=[('1-2', 'Half Width'), ('1-3', 'Third Width'), ('1-4', 'Quarter Width')]),
        ),
        migrations.AddField(
            model_name='article',
            name='link',
            field=models.ForeignKey(blank=True, null=True, related_name='article_link', to='block.Link'),
        ),
        migrations.AddField(
            model_name='article',
            name='references',
            field=models.ManyToManyField(to='block.Link'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_type',
            field=models.CharField(max_length=12, default='text_left', choices=[('text_left', 'Text Left'), ('text_right', 'Text Right'), ('text_top', 'Text Top'), ('text_bottom', 'Text Bottom'), ('text_only', 'Text Only'), ('picture_only', 'Picture Only')]),
        ),
    ]
