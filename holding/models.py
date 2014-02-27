# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

from cms.models import ContentModel


class HoldingContent(ContentModel):

    company = models.TextField()
    what_we_do = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='holding/%Y/%m/%d', blank=True)

    class Meta:
        # cannot put 'unique_together' on abstract base class
        # https://code.djangoproject.com/ticket/16732
        unique_together = ('container', 'moderate_state')
        verbose_name = 'Holding content'
        verbose_name_plural = 'Holding contents'

    def _get_content_set(self):
        return self.container.holdingcontent_set

    def __str__(self):
        return '{} {}'.format(self.company, self.moderate_state)

    def url_publish(self):
        return reverse('holding.content.publish', kwargs={'pk': self.pk})

    def url_remove(self):
        return reverse('project.stripe.remove', kwargs={'pk': self.pk})

    def url_update(self):
        return reverse('holding.content.update', kwargs={'pk': self.pk})


class TitleContent(ContentModel):

    """Just a title."""
    title = models.TextField()

    class Meta:
        # cannot put 'unique_together' on abstract base class
        # https://code.djangoproject.com/ticket/16732
        unique_together = ('container', 'moderate_state')
        verbose_name = 'Title'
        verbose_name_plural = 'Titles'

    def _get_content_set(self):
        return self.container.titlecontent_set

    def __str__(self):
        return '{} {}'.format(self.title, self.moderate_state)

    def url_publish(self):
        return reverse('holding.title.publish', kwargs={'pk': self.pk})

    def url_update(self):
        return reverse('holding.title.update', kwargs={'pk': self.pk})
