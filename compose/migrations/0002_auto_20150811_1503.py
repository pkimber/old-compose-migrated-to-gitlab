# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import block.models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0004_auto_20150810_1651'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('compose', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slideshow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('date_moderated', models.DateTimeField(blank=True, null=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('page_section', models.ForeignKey(to='block.PageSection')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Block',
                'verbose_name_plural': 'Blocks',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='image_size',
            field=models.CharField(default='1-2', choices=[('1-2', 'Half Width'), ('1-3', 'Third Width'), ('1-4', 'Quarter Width')], max_length=3),
        ),
        migrations.AddField(
            model_name='article',
            name='link',
            field=models.ForeignKey(to='block.Link', related_name='article_link', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_type',
            field=models.CharField(default='text_left', choices=[('text_left', 'Text Left'), ('text_right', 'Text Right'), ('text_top', 'Text Top'), ('text_bottom', 'Text Bottom'), ('text_only', 'Text Only'), ('picture_only', 'Picture Only')], max_length=12),
        ),
        migrations.AlterField(
            model_name='article',
            name='picture',
            field=models.ForeignKey(to='block.Image', related_name='article_picture', blank=True, null=True),
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
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+', blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='slideshow',
            unique_together=set([('block', 'moderate_state')]),
        ),
    ]
