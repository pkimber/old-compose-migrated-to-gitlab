# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from base.tests.model_maker import clean_and_save

from compose.models import (
    Article,
    ArticleBlock,
)


def make_article_block(page_section, **kwargs):
    defaults = dict(
        page_section=page_section,
    )
    defaults.update(kwargs)
    return clean_and_save(ArticleBlock(**defaults))


def make_article(block, order, title, **kwargs):
    defaults = dict(
        block=block,
        order=order,
        title=title,
    )
    defaults.update(kwargs)
    return clean_and_save(Article(**defaults))
