# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compose', '0006_auto_20150828_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeSnippet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(unique=True)),
                ('code', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Code Snippet',
                'verbose_name_plural': 'Code Snippets',
            },
        ),
    ]
