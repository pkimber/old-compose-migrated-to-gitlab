# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import block.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0002_auto_20141011_2223'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Holding',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('date_moderated', models.DateTimeField(null=True, blank=True)),
                ('order', models.IntegerField()),
                ('company', models.TextField()),
                ('what_we_do', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('logo', models.ImageField(upload_to='holding/%Y/%m/%d', blank=True)),
            ],
            options={
                'verbose_name': 'Holding content',
                'verbose_name_plural': 'Holding contents',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HoldingBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('page_section', models.ForeignKey(to='block.PageSection')),
            ],
            options={
                'verbose_name': 'Block',
                'verbose_name_plural': 'Blocks',
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('date_moderated', models.DateTimeField(null=True, blank=True)),
                ('order', models.IntegerField()),
                ('title', models.TextField()),
            ],
            options={
                'verbose_name': 'Title',
                'verbose_name_plural': 'Titles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TitleBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('page_section', models.ForeignKey(to='block.PageSection')),
            ],
            options={
                'verbose_name': 'Block',
                'verbose_name_plural': 'Blocks',
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='title',
            name='block',
            field=models.ForeignKey(related_name='content', to='holding.TitleBlock'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='title',
            name='edit_state',
            field=models.ForeignKey(to='block.EditState', default=block.models._default_edit_state_pk),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='title',
            name='moderate_state',
            field=models.ForeignKey(to='block.ModerateState', default=block.models._default_moderate_state_pk),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='title',
            name='user_moderated',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='title',
            unique_together=set([('block', 'moderate_state')]),
        ),
        migrations.AddField(
            model_name='holding',
            name='block',
            field=models.ForeignKey(related_name='content', to='holding.HoldingBlock'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='holding',
            name='edit_state',
            field=models.ForeignKey(to='block.EditState', default=block.models._default_edit_state_pk),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='holding',
            name='moderate_state',
            field=models.ForeignKey(to='block.ModerateState', default=block.models._default_moderate_state_pk),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='holding',
            name='user_moderated',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='holding',
            unique_together=set([('block', 'moderate_state')]),
        ),
    ]
