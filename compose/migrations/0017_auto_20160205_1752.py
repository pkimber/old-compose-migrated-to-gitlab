# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import block.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0011_auto_20151030_1551'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('compose', '0016_remove_feature_old_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sidebar',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('date_moderated', models.DateTimeField(blank=True, null=True)),
                ('order', models.IntegerField()),
                ('title', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Sidebars',
                'verbose_name': 'Sidebar',
            },
        ),
        migrations.CreateModel(
            name='SidebarBlock',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
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
        migrations.AddField(
            model_name='sidebar',
            name='block',
            field=models.ForeignKey(related_name='content', to='compose.SidebarBlock'),
        ),
        migrations.AddField(
            model_name='sidebar',
            name='edit_state',
            field=models.ForeignKey(to='block.EditState', default=block.models._default_edit_state),
        ),
        migrations.AddField(
            model_name='sidebar',
            name='moderate_state',
            field=models.ForeignKey(to='block.ModerateState', default=block.models._default_moderate_state),
        ),
        migrations.AddField(
            model_name='sidebar',
            name='user_moderated',
            field=models.ForeignKey(related_name='+', null=True, to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='sidebar',
            unique_together=set([('block', 'moderate_state')]),
        ),
    ]
