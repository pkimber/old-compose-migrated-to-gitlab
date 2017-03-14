# -*- encoding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.db import models

from reversion import revisions as reversion

from base.model_utils import TimeStampedModel
from block.models import (
    BlockModel,
    ContentModel,
    Image,
    Link,
    Wizard,
)


SECTION_BODY = 'body'
SECTION_CARD = 'card'
SECTION_GALLERY = 'gallery'
SECTION_NEWS = 'news'
SECTION_SLIDESHOW = 'slideshow'
SECTION_SIDEBAR = 'sidebar'


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

    title = models.CharField(max_length=200, blank=True)
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

    def text_size(self):
        invert = self.image_size.split('-')
        return '-'.join([str(int(invert[1])-int(invert[0])) or 1, invert[1]])

    @property
    def wizard_fields(self):
        return [
            Wizard('picture', Wizard.IMAGE, Wizard.SINGLE),
            Wizard('link', Wizard.LINK, Wizard.SINGLE),
        ]

reversion.register(Article)


class CodeSnippetManager(models.Manager):

    def create_code_snippet(self, slug, snippet):
        obj = self.model(slug=slug, code=snippet)
        obj.save()
        return obj

    def init_code_snippet(self, slug, snippet):
        try:
            obj = self.model.objects.get(slug=slug)
            obj.snippet = snippet
            obj.save()
        except ObjectDoesNotExist:
            obj = self.create_code_snippet(slug, snippet)
        return obj


class CodeSnippet(TimeStampedModel):

    CSS = 'css'

    slug = models.SlugField(unique=True)
    code = models.TextField(blank=True)
    objects = CodeSnippetManager()

    class Meta:
        verbose_name = 'Code Snippet'
        verbose_name_plural = 'Code Snippets'

    def __str__(self):
        return '{}'.format(self.slug)

reversion.register(CodeSnippet)


class SlideshowBlock(BlockModel):
    pass

reversion.register(SlideshowBlock)


class Slideshow(ContentModel):
    """Slideshow/carousel.

    Note from Tim: In the future you can extend slideshow model to include some
    basic slideshow options - like "Show controls" / "Speed" / "Auto Start"....
    even if we didn't use the same slider each time these properties would
    apply.

    Slideshow           Interim             Image
    ------------------- ------------------- -------------------
                        FK Slideshow        Order
                        FK Image            Image

    Use https://docs.djangoproject.com/en/1.8/topics/db/models/#intermediary-manytomany

    """

    block = models.ForeignKey(SlideshowBlock, related_name='content')
    order = models.IntegerField()

    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    slideshow = models.ManyToManyField(
        Image,
        related_name='slideshow',
        through='SlideshowImage'
    )

    class Meta:
        # cannot put 'unique_together' on abstract base class
        # https://code.djangoproject.com/ticket/16732
        unique_together = ('block', 'moderate_state')
        verbose_name = 'Slideshow'
        verbose_name_plural = 'Slideshow'

    def __str__(self):
        return '{} {}'.format(self.title, self.moderate_state)

    def copy_related_data(self, published_instance):
        """Copy slideshow images and links for the references."""
        for item in self.ordered_slideshow():
            obj = self.slideshow.through(
                content=published_instance,
                image=item.image,
                order=item.order,
            )
            obj.save()

    def ordered_slideshow(self):
        return self.slideshow.through.objects.filter(content=self)

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


class SlideshowImage(models.Model):
    """Slideshow images for the slideshow.

    This is the model that is used to govern the many-to-many relationship
    between ``Title`` and ``Image``.

    https://docs.djangoproject.com/en/1.8/topics/db/models/#extra-fields-on-many-to-many-relationships

    """
    content = models.ForeignKey(Slideshow)
    image = models.ForeignKey(Image)
    order = models.IntegerField()

    class Meta:
        ordering = ['order']
        verbose_name = 'Slideshow Image'
        verbose_name_plural = 'Slideshow Images'

reversion.register(SlideshowImage)


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

    SECTION_A = 'feature_a'
    SECTION_B = 'feature_b'
    SECTION_C = 'feature_c'
    SECTION_D = 'feature_d'

    block = models.ForeignKey(FeatureBlock, related_name='content')
    order = models.IntegerField()

    title = models.TextField()
    description = models.TextField(blank=True)
    picture = models.ForeignKey(
        Image,
        related_name='feature_picture',
        blank=True, null=True
    )
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

class SidebarBlock(BlockModel):
    pass

reversion.register(SidebarBlock)


class Sidebar(ContentModel):
    """Sidebar Block - title and style
    Used for heading for a section.
    """
    SECTION='sidebar'

    block = models.ForeignKey(SidebarBlock, related_name='content')
    order = models.IntegerField()

    title = models.TextField()

    class Meta:
        # cannot put 'unique_together' on abstract base class
        # https://code.djangoproject.com/ticket/16732
        unique_together = ('block', 'moderate_state')
        verbose_name = 'Sidebar'
        verbose_name_plural = 'Sidebars'

    def __str__(self):
        return '{} {}'.format(self.title, self.moderate_state)

    def url_publish(self):
        return reverse('compose.sidebar.publish', kwargs={'pk': self.pk})

    def url_remove(self):
        return reverse('compose.sidebar.remove', kwargs={'pk': self.pk})

    def url_update(self):
        return reverse('compose.sidebar.update', kwargs={'pk': self.pk})

reversion.register(Sidebar)
