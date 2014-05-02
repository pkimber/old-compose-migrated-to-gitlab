# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models

import reversion

from block.models import (
    BlockModel,
    ContentModel,
)


PAGE_HOME = 'home'
SECTION_BODY = 'body'
SECTION_FOOTER = 'footer'


class HoldingBlock(BlockModel):
    pass

reversion.register(HoldingBlock)


class Holding(ContentModel):

    block = models.ForeignKey(HoldingBlock, related_name='content')
    order = models.IntegerField()
    company = models.TextField()
    what_we_do = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='holding/%Y/%m/%d', blank=True)

    class Meta:
        # cannot put 'unique_together' on abstract base class
        # https://code.djangoproject.com/ticket/16732
        unique_together = ('block', 'moderate_state')
        verbose_name = 'Holding content'
        verbose_name_plural = 'Holding contents'

    def __str__(self):
        return '{}'.format(self.company)

    def url_publish(self):
        return reverse('holding.content.publish', kwargs={'pk': self.pk})

    def url_update(self):
        return reverse('holding.content.update', kwargs={'pk': self.pk})

reversion.register(Holding)


class TitleBlock(BlockModel):
    pass

reversion.register(TitleBlock)


class Title(ContentModel):
    """Just a title."""

    block = models.ForeignKey(TitleBlock, related_name='content')
    order = models.IntegerField()
    title = models.TextField()

    class Meta:
        # cannot put 'unique_together' on abstract base class
        # https://code.djangoproject.com/ticket/16732
        unique_together = ('block', 'moderate_state')
        verbose_name = 'Title'
        verbose_name_plural = 'Titles'

    def __str__(self):
        return '{}'.format(self.title)

    def url_publish(self):
        return reverse('holding.title.publish', kwargs={'pk': self.pk})

    def url_update(self):
        return reverse('holding.title.update', kwargs={'pk': self.pk})

reversion.register(Title)
