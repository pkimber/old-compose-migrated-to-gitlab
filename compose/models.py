# -*- encoding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models

import reversion

from base.model_utils import copy_model_instance
from block.models import (
    BlockModel,
    ContentModel,
    Image,
    Link,
    Wizard,
)


SECTION_BODY = 'body'
SECTION_CARD = 'card'
SECTION_SLIDESHOW = 'slideshow'


class ArticleBlock(BlockModel):
    pass

reversion.register(ArticleBlock)


class Article(ContentModel):

    ARTICLE_TYPE_CHOICES = (
        ('text_left', 'Text Left'),
        ('text_right', 'Text Right'),
        ('text_top', 'Text Top'),
        ('text_bottom', 'Text Bottom'),
        ('text_only', 'Text Only'),
        ('picture_only', 'Picture Only'),
    )

    IMAGE_SIZE = (
        ('1-2', 'Half Width'),
        ('1-3', 'Third Width'),
        ('1-4', 'Quarter Width'),
    )

    block = models.ForeignKey(ArticleBlock, related_name='content')
    order = models.IntegerField()

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    article_type = models.CharField(
        max_length=12,
        choices=ARTICLE_TYPE_CHOICES,
        default='text_left',
    )
    image_size = models.CharField(
        max_length=3,
        choices=IMAGE_SIZE,
        default='1-2',
    )
    link = models.ForeignKey(
        Link,
        related_name='article_link',
        blank=True, null=True
    )
    picture = models.ForeignKey(
        Image,
        related_name='article_picture',
        blank=True, null=True
    )

    class Meta:
        # cannot put 'unique_together' on abstract base class
        # https://code.djangoproject.com/ticket/16732
        unique_together = ('block', 'moderate_state')
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return '{} {}'.format(self.title, self.moderate_state)

    def url_publish(self):
        return reverse('compose.article.publish', kwargs={'pk': self.pk})

    def url_remove(self):
        return reverse('compose.article.remove', kwargs={'pk': self.pk})

    def url_update(self):
        return reverse('compose.article.update', kwargs={'pk': self.pk})

    @property
    def wizard_fields(self):
        return [
            Wizard('picture', Wizard.IMAGE, Wizard.SINGLE),
            Wizard('link', Wizard.LINK, Wizard.SINGLE),
        ]

reversion.register(Article)


class SlideshowBlock(BlockModel):
    pass

reversion.register(SlideshowBlock)


class Slideshow(ContentModel):
    """Slideshow/carousel.

    Note from Tim: In the future you can extend slideshow model to include some
    basic slideshow options - like "Show controls" / "Speed" / "Auto Start"....
    even if we didn't use the same slider each time these properties would
    apply.

    """

    block = models.ForeignKey(SlideshowBlock, related_name='content')
    order = models.IntegerField()

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    slideshow = models.ManyToManyField(Image)

    class Meta:
        # cannot put 'unique_together' on abstract base class
        # https://code.djangoproject.com/ticket/16732
        unique_together = ('block', 'moderate_state')
        verbose_name = 'Slideshow'
        verbose_name_plural = 'Slideshow'

    def __str__(self):
        return '{} {}'.format(self.title, self.moderate_state)

    def copy_related_data(self, published_instance):
        """Copy slideshow images."""
        for image in self.slideshow.all():
            published_instance.slideshow.add(image)

    def url_publish(self):
        return reverse('compose.slideshow.publish', kwargs={'pk': self.pk})

    def url_remove(self):
        return reverse('compose.slideshow.remove', kwargs={'pk': self.pk})

    def url_update(self):
        return reverse('compose.slideshow.update', kwargs={'pk': self.pk})

    @property
    def wizard_fields(self):
        return [
            Wizard('slideshow', Wizard.IMAGE, Wizard.MULTI),
        ]

reversion.register(Slideshow)


class FeatureBlock(BlockModel):
    pass

reversion.register(FeatureBlock)


class FeatureStyle(models.Model):
    """Select Feature CSS class."""

    name = models.CharField(max_length=100)
    css_class_name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Feature Style'
        verbose_name_plural = 'Feature Styles'

    def __str__(self):
        return '{}'.format(self.name)

reversion.register(FeatureStyle)


class Feature(ContentModel):
    """Feature Block title, description (plain text), picture, URL style
    Used where we are providing a some links that we want to feature.
    """

    SECTION_A='feature_a'
    SECTION_B='feature_b'
    SECTION_C='feature_c'
    SECTION_D='feature_d'

    block = models.ForeignKey(FeatureBlock, related_name='content')
    order = models.IntegerField()

    title = models.TextField()
    description = models.TextField(blank=True)
    picture = models.ImageField(upload_to='block', blank=True)
    link = models.ForeignKey(
        Link,
        related_name='feature_link',
        blank=True, null=True
    )
    style = models.ForeignKey(FeatureStyle, blank=True, null=True)

    class Meta:
        # cannot put 'unique_together' on abstract base class
        # https://code.djangoproject.com/ticket/16732
        unique_together = ('block', 'moderate_state')
        verbose_name = 'Feature block'
        verbose_name_plural = 'Feature blocks'

    def __str__(self):
        return '{} {}'.format(self.title, self.moderate_state)

    def set_url(self, url_link, url_text):
        self.url = url_link

    def get_url_link(self):
        return self.url

    def get_url_text(self):
        return None

    def url_publish(self):
        return reverse('compose.feature.publish', kwargs={'pk': self.pk})

    def url_remove(self):
        return reverse('compose.feature.remove', kwargs={'pk': self.pk})

    def url_update(self):
        return reverse('compose.feature.update', kwargs={'pk': self.pk})

    def css_class_name(self):
        if self.style:
            return self.style.css_class_name
        else:
            return ''

    @property
    def wizard_fields(self):
        return [
            Wizard('picture', Wizard.IMAGE, Wizard.SINGLE),
            Wizard('link', Wizard.LINK, Wizard.SINGLE),
        ]

reversion.register(Feature)


class HeaderStyle(models.Model):
    """Select Header CSS class."""

    name = models.CharField(max_length=100)
    css_class_name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Header style'
        verbose_name_plural = 'Header styles'

    def __str__(self):
        return '{}'.format(self.name)

reversion.register(HeaderStyle)


class HeaderBlock(BlockModel):
    pass

reversion.register(HeaderBlock)


class Header(ContentModel):
    """Header Block - title and style
    Used for heading for a section.
    """
    SECTION_A='header_a'
    SECTION_B='header_b'
    SECTION_C='header_c'
    SECTION_D='header_d'

    block = models.ForeignKey(HeaderBlock, related_name='content')
    order = models.IntegerField()

    title = models.TextField()
    style = models.ForeignKey(HeaderStyle, blank=True, null=True)

    class Meta:
        # cannot put 'unique_together' on abstract base class
        # https://code.djangoproject.com/ticket/16732
        unique_together = ('block', 'moderate_state')
        verbose_name = 'Header'
        verbose_name_plural = 'Headers'

    def __str__(self):
        return '{} {}'.format(self.title, self.moderate_state)

    def url_publish(self):
        return reverse('compose.header.publish', kwargs={'pk': self.pk})

    def url_remove(self):
        return reverse('compose.header.remove', kwargs={'pk': self.pk})

    def url_update(self):
        return reverse('compose.header.update', kwargs={'pk': self.pk})

    def css_class_name(self):
        if self.style:
            return self.style.css_class_name
        else:
            return ''

reversion.register(Header)
