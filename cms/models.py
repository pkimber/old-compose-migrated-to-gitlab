# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import reversion

from base.model_utils import TimeStampedModel
from base.singleton import SingletonModel
from block.models import (
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


class Template(TimeStampedModel):

    template_name = models.CharField(
        max_length=150,
        help_text="File name e.g. 'compose/page_article.html'",
    )

    class Meta:
        ordering = ('template_name',)
        verbose_name = 'Template'
        verbose_name_plural = 'Templates'

    def __str__(self):
        return '{}'.format(self.template_name)

    def setup_page(self, page):
        page.template_name = self.template_name
        page.pagesection_set.all().delete()
        for template_section in self.templatesection_set.all():
            page_section = PageSection(
                page=page,
                section=template_section.section,
            )
            page_section.save()
        page.save()

reversion.register(Template)


class TemplateSection(TimeStampedModel):

    template = models.ForeignKey(Template)
    section = models.ForeignKey(Section)

    class Meta:
        ordering = ('template__template_name', 'section__name')
        unique_together = ('template', 'section')
        verbose_name = 'Template section'
        verbose_name_plural = 'Template sections'

    def __str__(self):
        return '{}, {}'.format(self.template.template_name, self.section.name)

reversion.register(TemplateSection)
