# -*- encoding: utf-8 -*-
import factory

from block.tests.factories import PageSectionFactory
from compose.models import (
    Article,
    ArticleBlock,
    CodeSnippet,
    Slideshow,
    SlideshowBlock,
    SlideshowImage,
    #Feature,
    #FeatureBlock,
    #Header,
    #HeaderBlock,
)


class ArticleBlockFactory(factory.django.DjangoModelFactory):

    page_section = factory.SubFactory(PageSectionFactory)

    class Meta:
        model = ArticleBlock


class ArticleFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Article

    block = factory.SubFactory(ArticleBlockFactory)

    @factory.sequence
    def order(n):
        return n


class CodeSnippetFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = CodeSnippet

    @factory.sequence
    def slug(n):
        return 'slug_{:02d}'.format(n)


class SlideshowBlockFactory(factory.django.DjangoModelFactory):

    page_section = factory.SubFactory(PageSectionFactory)

    class Meta:
        model = SlideshowBlock


class SlideshowImageFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = SlideshowImage


class SlideshowFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Slideshow

    block = factory.SubFactory(SlideshowBlockFactory)

    @factory.sequence
    def order(n):
        return n


#class FeatureBlockFactory(factory.django.DjangoModelFactory):
#
#    page_section = factory.SubFactory(PageSectionFactory)
#
#    class Meta:
#        model = FeatureBlock
#
#
#class FeatureFactory(factory.django.DjangoModelFactory):
#
#    class Meta:
#        model = Feature
#
#    block = factory.SubFactory(FeatureBlockFactory)
#
#    @factory.sequence
#    def order(n):
#        return n
#
#
#class HeaderBlockFactory(factory.django.DjangoModelFactory):
#
#    page_section = factory.SubFactory(PageSectionFactory)
#
#    class Meta:
#        model = HeaderBlock
#
#
#class HeaderFactory(factory.django.DjangoModelFactory):
#
#    class Meta:
#        model = Header
#
#    block = factory.SubFactory(HeaderBlockFactory)
#
#    @factory.sequence
#    def order(n):
#        return n
