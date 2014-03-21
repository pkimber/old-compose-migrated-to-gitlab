# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from block.models import (
    BlockError,
    ModerateState,
    Page,
)
from block.service import (
    init_page,
    init_section,
)
from block.tests.scenario import default_moderate_state

from holding.models import (
    Holding,
    HoldingBlock,
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
    return Page.objects.get(slug='home')


def _init_holding_block(page, section):
    try:
        result = HoldingBlock.objects.get(page=page, section=section)
    except HoldingBlock.DoesNotExist:
        print("make_holding_block: {}.{}".format(page.name, section.name))
        result = make_holding_block(page, section)
    return result


def _init_title_block(page, section):
    try:
        result = TitleBlock.objects.get(page=page, section=section)
    except TitleBlock.DoesNotExist:
        print("make_title_block: {}.{}".format(page.name, section.name))
        result = make_title_block(page, section)
    return result


def _init_footer(block, title):
    """Create a footer - if there isn't one already."""
    result = Title.objects.filter(block=block)
    if result:
        return result[0]
    else:
        print("make_title: {}".format(title))
        return make_title(block, 1, ModerateState.pending(), title)


def _init_holding(block, company):
    """Create a main content section - if there isn't one already."""
    result = Holding.objects.filter(block=block)
    if result:
        return result[0]
    else:
        print("make_holding: {}".format(company))
        return make_holding(block, 1, ModerateState.pending(), company)


def init_app_holding():
    default_moderate_state()
    # page
    home = init_page('Home', 0, is_home=True)
    # layout
    body = init_section('Body')
    footer = init_section('Footer')
    # holding
    holding_block = _init_holding_block(home, body)
    _init_holding(holding_block, 'Your Company Name')
    # footer
    title_block = _init_title_block(home, footer)
    _init_footer(title_block, 'Please edit this footer...')
