# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

import factory

from block.tests.factories import PageSectionFactory
from holding.models import (
    Holding,
    HoldingBlock,
    Title,
    TitleBlock,
)


class HoldingBlockFactory(factory.django.DjangoModelFactory):

    page_section = factory.SubFactory(PageSectionFactory)

    class Meta:
        model = HoldingBlock


class HoldingFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Holding

    block = factory.SubFactory(HoldingBlockFactory)

    @factory.sequence
    def order(n):
        return n


class TitleBlockFactory(factory.django.DjangoModelFactory):

    page_section = factory.SubFactory(PageSectionFactory)

    class Meta:
        model = TitleBlock


class TitleFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Title

    block = factory.SubFactory(TitleBlockFactory)

    @factory.sequence
    def order(n):
        return n
