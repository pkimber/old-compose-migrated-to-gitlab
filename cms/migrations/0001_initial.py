# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0002_auto_20141011_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderFooter',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('header', models.CharField(max_length=150)),
                ('url_twitter', models.URLField(verbose_name='Twitter URL', blank=True)),
                ('url_linkedin', models.URLField(verbose_name='LinkedIn URL', blank=True)),
            ],
            options={
                'verbose_name': 'Header and footer',
                'verbose_name_plural': 'Header and footers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('template_name', models.CharField(max_length=150, help_text="File name e.g. 'compose/page_article.html'")),
            ],
            options={
                'ordering': ('template_name',),
                'verbose_name': 'Template',
                'verbose_name_plural': 'Templates',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TemplateSection',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('section', models.ForeignKey(to='block.Section')),
                ('template', models.ForeignKey(to='cms.Template')),
            ],
            options={
                'ordering': ('template__template_name', 'section__name'),
                'verbose_name': 'Template section',
                'verbose_name_plural': 'Template sections',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='templatesection',
            unique_together=set([('template', 'section')]),
        ),
    ]
