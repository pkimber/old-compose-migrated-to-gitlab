# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import block.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('block', '0004_auto_20150810_1651'),
        ('compose', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slideshow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('date_moderated', models.DateTimeField(null=True, blank=True)),
                ('order', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Slideshow',
                'verbose_name_plural': 'Slideshow',
            },
        ),
        migrations.CreateModel(
            name='SlideshowBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('page_section', models.ForeignKey(to='block.PageSection')),
            ],
            options={
                'verbose_name': 'Block',
                'abstract': False,
                'verbose_name_plural': 'Blocks',
            },
        ),
        migrations.RenameField(
            model_name='article',
            old_name='picture',
            new_name='picture_old',
        ),
        migrations.AddField(
            model_name='slideshow',
            name='block',
            field=models.ForeignKey(to='compose.SlideshowBlock', related_name='content'),
        ),
        migrations.AddField(
            model_name='slideshow',
            name='edit_state',
            field=models.ForeignKey(default=block.models._default_edit_state, to='block.EditState'),
        ),
        migrations.AddField(
            model_name='slideshow',
            name='moderate_state',
            field=models.ForeignKey(default=block.models._default_moderate_state, to='block.ModerateState'),
        ),
        migrations.AddField(
            model_name='slideshow',
            name='slideshow',
            field=models.ManyToManyField(to='block.Image'),
        ),
        migrations.AddField(
            model_name='slideshow',
            name='user_moderated',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+', null=True, blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='slideshow',
            unique_together=set([('block', 'moderate_state')]),
        ),
    ]
