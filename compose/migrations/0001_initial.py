# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import block.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0003_auto_20150419_2130'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('date_moderated', models.DateTimeField(blank=True, null=True)),
                ('order', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='compose')),
                ('article_type', models.CharField(choices=[('text_left', 'Text Left'), ('text_right', 'Text Right'), ('text_only', 'Text Only'), ('picture_only', 'Picture Only')], max_length=12, default='text_left')),
            ],
            options={
                'verbose_name_plural': 'Articles',
                'verbose_name': 'Article',
            },
        ),
        migrations.CreateModel(
            name='ArticleBlock',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('page_section', models.ForeignKey(to='block.PageSection')),
            ],
            options={
                'verbose_name_plural': 'Blocks',
                'verbose_name': 'Block',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='article',
            name='block',
            field=models.ForeignKey(related_name='content', to='compose.ArticleBlock'),
        ),
        migrations.AddField(
            model_name='article',
            name='edit_state',
            field=models.ForeignKey(to='block.EditState', default=block.models._default_edit_state),
        ),
        migrations.AddField(
            model_name='article',
            name='moderate_state',
            field=models.ForeignKey(to='block.ModerateState', default=block.models._default_moderate_state),
        ),
        migrations.AddField(
            model_name='article',
            name='user_moderated',
            field=models.ForeignKey(blank=True, related_name='+', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='article',
            unique_together=set([('block', 'moderate_state')]),
        ),
    ]
