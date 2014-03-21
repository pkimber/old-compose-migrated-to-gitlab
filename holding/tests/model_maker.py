# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from base.tests.model_maker import clean_and_save

from holding.models import (
    Holding,
    HoldingBlock,
    Title,
    TitleBlock,
)


def make_holding_block(page, section, **kwargs):
    defaults = dict(
        page=page,
        section=section,
    )
    defaults.update(kwargs)
    return clean_and_save(HoldingBlock(**defaults))


def make_holding(block, order, moderate_state, company, **kwargs):
    defaults = dict(
        block=block,
        order=order,
        moderate_state=moderate_state,
        company=company,
    )
    defaults.update(kwargs)
    return clean_and_save(Holding(**defaults))


def make_title_block(page, section, **kwargs):
    defaults = dict(
        page=page,
        section=section,
    )
    defaults.update(kwargs)
    return clean_and_save(TitleBlock(**defaults))


def make_title(block, order, moderate_state, title, **kwargs):
    defaults = dict(
        block=block,
        order=order,
        moderate_state=moderate_state,
        title=title,
    )
    defaults.update(kwargs)
    return clean_and_save(Title(**defaults))
