# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from block.models import (
    BlockError,
    Page,
)
from block.service import (
    init_page,
    init_page_section,
    init_section,
)
from block.tests.scenario import init_app_block

from holding.models import (
    Holding,
    HoldingBlock,
    PAGE_HOME,
    SECTION_BODY,
    SECTION_FOOTER,
    Title,
    TitleBlock,
)
from holding.tests.model_maker import (
    make_holding,
    make_holding_block,
    make_title,
    make_title_block,
)


def get_title_content():
    result = Title.objects.all()
    if result:
        return result[0]
    else:
        raise BlockError("Cannot find any title content")


def get_holding_content():
    result = Holding.objects.all()
    if result:
        return result[0]
    else:
        raise BlockError("Cannot find any holding content")


def get_page_home():
    return Page.objects.get(slug=PAGE_HOME)


def _init_holding_block(page_section):
    try:
        result = HoldingBlock.objects.get(page_section=page_section)
    except HoldingBlock.DoesNotExist:
        print("make_holding_block: {}".format(page_section))
        result = make_holding_block(page_section)
    return result


def _init_title_block(page_section):
    try:
        result = TitleBlock.objects.get(page_section=page_section)
    except TitleBlock.DoesNotExist:
        print("make_title_block: {}".format(page_section))
        result = make_title_block(page_section)
    return result


def _init_footer(block, title):
    """Create a footer - if there isn't one already."""
    result = Title.objects.filter(block=block)
    if result:
        return result[0]
    else:
        print("make_title: {}".format(title))
        return make_title(block, 1, title)


def _init_holding(block, company):
    """Create a main content section - if there isn't one already."""
    result = Holding.objects.filter(block=block)
    if result:
        return result[0]
    else:
        print("make_holding: {}".format(company))
        return make_holding(block, 1, company)


def init_app_holding():
    init_app_block()
    # page
    # name, slug_page, order, template_name, is_home=None, slug_menu=None):
    home = init_page(
        'Home',
        PAGE_HOME,
        0,
        'holding/page_content.html',
        is_home=True,
    )
    # layout
    body = init_section(
        SECTION_BODY.capitalize(),
        'holding',
        'Holding',
        None,
    )
    footer = init_section(
        SECTION_FOOTER.capitalize(),
        'holding',
        'Title',
        None,
    )
    home_body = init_page_section(home, body)
    home_footer = init_page_section(home, footer)
    # holding
    holding_block = _init_holding_block(home_body)
    _init_holding(holding_block, 'Your Company Name')
    # footer
    title_block = _init_title_block(home_footer)
    _init_footer(title_block, 'Please edit this footer...')
