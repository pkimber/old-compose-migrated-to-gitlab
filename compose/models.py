# -*- encoding: utf-8 -*-
from django.conf import settings
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


H1 = 'h1'
H2 = 'h2'
H3 = 'h3'
H4 = 'h4'

HEADING_LEVELS = (
    (H1, H1),
    (H2, H2),
    (H3, H3),
    (H4, H4),
)

SECTION_BODY = 'body'
SECTION_CARD = 'card'
SECTION_GALLERY = 'gallery'
SECTION_NEWS = 'news'
SECTION_SLIDESHOW = 'slideshow'
SECTION_SIDEBAR = 'sidebar'


class ContentBase(ContentModel):

    heading_level = models.CharField(max_length=2,
        choices=HEADING_LEVELS,
        default=H2,
    )
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    css_width = models.CharField(
        max_length=12,
        choices=settings.CSS_WIDTHS,
        default=settings.CSS_WIDTH_HALFBIG,
    )

    class Meta:
        abstract = True


class ArticleBlock(BlockModel):
    pass

reversion.register(ArticleBlock)


class Article(ContentBase):

    block = models.ForeignKey(ArticleBlock, related_name='content')

    article_type = models.CharField(
        max_length=64,
        choices=settings.CSS_TEXT_POSITION,
        default=settings.CSS_TEXT_LEFT,
    )
    image_size = models.CharField(
        max_length=64,
        choices=settings.CSS_IMAGE_SIZES,
        default=settings.CSS_IMAGE_SIZE_HALF,
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

    def url_order_up(self):
        if self.order > 1:
            return reverse('compose.article.up', kwargs={'pk': self.pk})
        else:
            return '#'

    def url_order_down(self):
        max_order = Article.objects.get_max_order(self.block)
        if self.order < max_order:
            return reverse('compose.article.down', kwargs={'pk': self.pk})
        else:
            return '#'

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


class Slideshow(ContentBase):
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


class Feature(ContentBase):
    """Feature Block title, description (plain text), picture, URL style
    Used where we are providing a some links that we want to feature.
    """

    SECTION_A = 'feature_a'
    SECTION_B = 'feature_b'
    SECTION_C = 'feature_c'
    SECTION_D = 'feature_d'

    block = models.ForeignKey(FeatureBlock, related_name='content')

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
