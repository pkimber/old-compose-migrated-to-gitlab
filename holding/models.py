from django.core.urlresolvers import reverse
from django.db import models

from cms.models import ContentModel


class HoldingContent(ContentModel):

    title = models.TextField()
    heading = models.TextField()
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='holding/%Y/%m/%d', blank=True)

    class Meta:
        # cannot put 'unique_together' on abstract base class
        # https://code.djangoproject.com/ticket/16732
        unique_together = ('container', 'moderate_state')
        verbose_name = 'Holding content'
        verbose_name_plural = 'Holding contents'

    def _get_content_set(self):
        return self.container.holdingcontent_set

    def __unicode__(self):
        return unicode('{} {}'.format(self.title, self.moderate_state))

    def url_publish(self):
        return reverse('project.stripe.publish', kwargs={'pk': self.pk})

    def url_remove(self):
        return reverse('project.stripe.remove', kwargs={'pk': self.pk})

    def url_update(self):
        return reverse('project.stripe.update', kwargs={'pk': self.pk})


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

    def __unicode__(self):
        return unicode('{} {}'.format(self.title, self.moderate_state))

    def url_publish(self):
        return reverse('holding.title.publish', kwargs={'pk': self.pk})

    def url_remove(self):
        return reverse('project.title.remove', kwargs={'pk': self.pk})

    def url_update(self):
        return reverse('holding.title.update', kwargs={'pk': self.pk})
