# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from base.tests.model_maker import clean_and_save

from holding.models import (
    HoldingContent,
    TitleContent,
)


def make_holding_content(container, moderate_state, company, **kwargs):
    defaults = dict(
        container=container,
        moderate_state=moderate_state,
        company=company,
    )
    defaults.update(kwargs)
    return clean_and_save(HoldingContent(**defaults))


def make_title_content(container, moderate_state, title, **kwargs):
    defaults = dict(
        container=container,
        moderate_state=moderate_state,
        title=title,
    )
    defaults.update(kwargs)
    return clean_and_save(TitleContent(**defaults))
