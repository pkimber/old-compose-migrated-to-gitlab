# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import block.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('block', '0004_linkdocument_linkimage'),
        ('compose', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('date_moderated', models.DateTimeField(blank=True, null=True)),
                ('order', models.IntegerField()),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('picture', models.ImageField(upload_to='block', blank=True)),
                ('url', models.URLField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Feature block',
                'verbose_name_plural': 'Feature blocks',
            },
        ),
        migrations.CreateModel(
            name='FeatureBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
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
        migrations.CreateModel(
            name='FeatureStyle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('css_class_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Feature Style',
                'ordering': ('name',),
                'verbose_name_plural': 'Feature Styles',
            },
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
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
        migrations.CreateModel(
            name='HeaderStyle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('css_class_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Header style',
                'ordering': ('name',),
                'verbose_name_plural': 'Header styles',
            },
        ),
        migrations.RemoveField(
            model_name='article',
            name='picture',
        ),
        migrations.AddField(
            model_name='article',
            name='link_document',
            field=models.ForeignKey(blank=True, null=True, to='block.LinkDocument'),
        ),
        migrations.AddField(
            model_name='article',
            name='link_image',
            field=models.ForeignKey(blank=True, null=True, to='block.LinkImage'),
        ),
        migrations.AddField(
            model_name='header',
            name='block',
            field=models.ForeignKey(related_name='content', to='compose.HeaderBlock'),
        ),
        migrations.AddField(
            model_name='header',
            name='edit_state',
            field=models.ForeignKey(default=block.models._default_edit_state, to='block.EditState'),
        ),
        migrations.AddField(
            model_name='header',
            name='moderate_state',
            field=models.ForeignKey(default=block.models._default_moderate_state, to='block.ModerateState'),
        ),
        migrations.AddField(
            model_name='header',
            name='style',
            field=models.ForeignKey(blank=True, null=True, to='compose.HeaderStyle'),
        ),
        migrations.AddField(
            model_name='header',
            name='user_moderated',
            field=models.ForeignKey(related_name='+', blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feature',
            name='block',
            field=models.ForeignKey(related_name='content', to='compose.FeatureBlock'),
        ),
        migrations.AddField(
            model_name='feature',
            name='edit_state',
            field=models.ForeignKey(default=block.models._default_edit_state, to='block.EditState'),
        ),
        migrations.AddField(
            model_name='feature',
            name='moderate_state',
            field=models.ForeignKey(default=block.models._default_moderate_state, to='block.ModerateState'),
        ),
        migrations.AddField(
            model_name='feature',
            name='style',
            field=models.ForeignKey(blank=True, null=True, to='compose.FeatureStyle'),
        ),
        migrations.AddField(
            model_name='feature',
            name='user_moderated',
            field=models.ForeignKey(related_name='+', blank=True, null=True, to=settings.AUTH_USER_MODEL),
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
