# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

import factory

from block.tests.factories import PageSectionFactory
from compose.models import (
    Article,
    ArticleBlock,
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
