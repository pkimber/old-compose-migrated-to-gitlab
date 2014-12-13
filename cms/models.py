# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import reversion

from base.model_utils import TimeStampedModel
from base.singleton import SingletonModel
from block.models import (
    Page,
    PageSection,
    Section,
)


class HeaderFooter(SingletonModel):

    header = models.CharField(max_length=150)
    #footer_left = models.TextField(blank=True)
    #footer_right = models.TextField(blank=True)
    url_twitter = models.URLField(verbose_name='Twitter URL', blank=True)
    url_linkedin = models.URLField(verbose_name='LinkedIn URL', blank=True)

    class Meta:
        verbose_name = 'Header and footer'
        verbose_name_plural = 'Header and footers'

    def __str__(self):
        return '{}'.format(self.header)

reversion.register(HeaderFooter)


class TemplateManager(models.Manager):

    def create_template(self, template_name):
        template = self.model(template_name=template_name)
        template.save()
        return template

    def init_template(self, template_name):
        templates = self.model.objects.filter(template_name=template_name)
        if templates:
            result = templates[0]
        else:
            result = self.create_template(template_name)
        return result


class Template(TimeStampedModel):

    template_name = models.CharField(
        max_length=150,
        help_text="File name e.g. 'compose/page_article.html'",
    )
    objects = TemplateManager()

    class Meta:
        ordering = ('template_name',)
        verbose_name = 'Template'
        verbose_name_plural = 'Templates'

    def __str__(self):
        return '{}'.format(self.template_name)

    def update_page(self, page):
        page.template_name = self.template_name
        page.pagesection_set.all().delete()
        for template_section in self.templatesection_set.all():
            page_section = PageSection(
                page=page,
                section=template_section.section,
            )
            page_section.save()
        page.save()

    def update_pages(self):
        for p in Page.objects.filter(template_name=self.template_name):
            self.update_page(p)

reversion.register(Template)


class TemplateSectionManager(models.Manager):

    def create_template_section(self, template, section):
        template_section = self.model(template=template, section=section)
        template_section.save()
        return template_section

    def init_template_section(self, template, section):
        try:
            template_section = self.model.objects.get(
                template=template,
                section=section,
            )
        except self.model.DoesNotExist:
            template_section = self.create_template_section(template, section)
        return template_section


class TemplateSection(TimeStampedModel):

    template = models.ForeignKey(Template)
    section = models.ForeignKey(Section)
    objects = TemplateSectionManager()

    class Meta:
        ordering = ('template__template_name', 'section__name')
        unique_together = ('template', 'section')
        verbose_name = 'Template section'
        verbose_name_plural = 'Template sections'

    def __str__(self):
        return '{}, {}'.format(self.template.template_name, self.section.name)

reversion.register(TemplateSection)
