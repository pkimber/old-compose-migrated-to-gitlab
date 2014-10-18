# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from base.tests.model_maker import clean_and_save

from cms.models import (
    Holding,
    HoldingBlock,
    Title,
    TitleBlock,
)


def make_holding_block(page_section, **kwargs):
    defaults = dict(
        page_section=page_section,
    )
    defaults.update(kwargs)
    return clean_and_save(HoldingBlock(**defaults))


def make_holding(block, order, company, **kwargs):
    defaults = dict(
        block=block,
        order=order,
        company=company,
    )
    defaults.update(kwargs)
    return clean_and_save(Holding(**defaults))


def make_title_block(page_section, **kwargs):
    defaults = dict(
        page_section=page_section,
    )
    defaults.update(kwargs)
    return clean_and_save(TitleBlock(**defaults))


def make_title(block, order, title, **kwargs):
    defaults = dict(
        block=block,
        order=order,
        title=title,
    )
    defaults.update(kwargs)
    return clean_and_save(Title(**defaults))
