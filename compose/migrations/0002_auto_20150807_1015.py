# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import block.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('block', '0004_link_linkimage'),
        ('compose', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('date_moderated', models.DateTimeField(blank=True, null=True)),
                ('order', models.IntegerField()),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('picture', models.ImageField(upload_to='block', blank=True)),
                ('url', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Feature block',
                'verbose_name_plural': 'Feature blocks',
            },
        ),
        migrations.CreateModel(
            name='FeatureBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('page_section', models.ForeignKey(to='block.PageSection')),
            ],
            options={
                'verbose_name': 'Block',
                'verbose_name_plural': 'Blocks',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FeatureStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('css_class_name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Feature Style',
                'verbose_name_plural': 'Feature Styles',
            },
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('date_moderated', models.DateTimeField(blank=True, null=True)),
                ('order', models.IntegerField()),
                ('title', models.TextField()),
            ],
            options={
                'verbose_name': 'Header',
                'verbose_name_plural': 'Headers',
            },
        ),
        migrations.CreateModel(
            name='HeaderBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('page_section', models.ForeignKey(to='block.PageSection')),
            ],
            options={
                'verbose_name': 'Block',
                'verbose_name_plural': 'Blocks',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HeaderStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('css_class_name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Header style',
                'verbose_name_plural': 'Header styles',
            },
        ),
        migrations.RemoveField(
            model_name='article',
            name='picture',
        ),
        migrations.AddField(
            model_name='article',
            name='link',
            field=models.ForeignKey(to='block.Link', related_name='article_link', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='link_image',
            field=models.ForeignKey(to='block.LinkImage', related_name='article_link_image', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='link_images',
            field=models.ManyToManyField(to='block.LinkImage'),
        ),
        migrations.AddField(
            model_name='article',
            name='links',
            field=models.ManyToManyField(to='block.Link'),
        ),
        migrations.AddField(
            model_name='header',
            name='block',
            field=models.ForeignKey(to='compose.HeaderBlock', related_name='content'),
        ),
        migrations.AddField(
            model_name='header',
            name='edit_state',
            field=models.ForeignKey(to='block.EditState', default=block.models._default_edit_state),
        ),
        migrations.AddField(
            model_name='header',
            name='moderate_state',
            field=models.ForeignKey(to='block.ModerateState', default=block.models._default_moderate_state),
        ),
        migrations.AddField(
            model_name='header',
            name='style',
            field=models.ForeignKey(to='compose.HeaderStyle', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='header',
            name='user_moderated',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='block',
            field=models.ForeignKey(to='compose.FeatureBlock', related_name='content'),
        ),
        migrations.AddField(
            model_name='feature',
            name='edit_state',
            field=models.ForeignKey(to='block.EditState', default=block.models._default_edit_state),
        ),
        migrations.AddField(
            model_name='feature',
            name='moderate_state',
            field=models.ForeignKey(to='block.ModerateState', default=block.models._default_moderate_state),
        ),
        migrations.AddField(
            model_name='feature',
            name='style',
            field=models.ForeignKey(to='compose.FeatureStyle', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='user_moderated',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+', null=True, blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='header',
            unique_together=set([('block', 'moderate_state')]),
        ),
        migrations.AlterUniqueTogether(
            name='feature',
            unique_together=set([('block', 'moderate_state')]),
        ),
    ]
