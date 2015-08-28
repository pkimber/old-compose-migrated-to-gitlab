# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import block.models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0007_auto_20150821_2228'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('compose', '0005_remove_article_picture_old'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('date_moderated', models.DateTimeField(null=True, blank=True)),
                ('order', models.IntegerField()),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('picture', models.ImageField(upload_to='block', blank=True)),
                ('url', models.URLField(null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Feature blocks',
                'verbose_name': 'Feature block',
            },
        ),
        migrations.CreateModel(
            name='FeatureBlock',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('page_section', models.ForeignKey(to='block.PageSection')),
            ],
            options={
                'verbose_name_plural': 'Blocks',
                'abstract': False,
                'verbose_name': 'Block',
            },
        ),
        migrations.CreateModel(
            name='FeatureStyle',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('css_class_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Feature Styles',
                'ordering': ('name',),
                'verbose_name': 'Feature Style',
            },
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('date_moderated', models.DateTimeField(null=True, blank=True)),
                ('order', models.IntegerField()),
                ('title', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Headers',
                'verbose_name': 'Header',
            },
        ),
        migrations.CreateModel(
            name='HeaderBlock',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('page_section', models.ForeignKey(to='block.PageSection')),
            ],
            options={
                'verbose_name_plural': 'Blocks',
                'abstract': False,
                'verbose_name': 'Block',
            },
        ),
        migrations.CreateModel(
            name='HeaderStyle',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('css_class_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Header styles',
                'ordering': ('name',),
                'verbose_name': 'Header style',
            },
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
            field=models.ForeignKey(null=True, blank=True, to='compose.HeaderStyle'),
        ),
        migrations.AddField(
            model_name='header',
            name='user_moderated',
            field=models.ForeignKey(null=True, related_name='+', blank=True, to=settings.AUTH_USER_MODEL),
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
            field=models.ForeignKey(null=True, blank=True, to='compose.FeatureStyle'),
        ),
        migrations.AddField(
            model_name='feature',
            name='user_moderated',
            field=models.ForeignKey(null=True, related_name='+', blank=True, to=settings.AUTH_USER_MODEL),
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
