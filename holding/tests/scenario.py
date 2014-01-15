from cms.models import ModerateState
from cms.service import (
    init_container,
    init_layout,
    init_page,
    init_section,
)
from cms.tests.scenario import default_moderate_state

from holding.models import (
    HoldingContent,
    TitleContent,
)
from holding.tests.model_maker import (
    make_holding_content,
    make_title_content,
)


def get_title_content():
    result = TitleContent.objects.all()
    if result:
        return result[0]
    else:
        raise CmsError("Cannot find any title content")


def get_holding_content():
    result = HoldingContent.objects.all()
    if result:
        return result[0]
    else:
        raise CmsError("Cannot find any holding content")


def _init_footer(container, title):
    """Create a footer - if there isn't one already."""
    result = TitleContent.objects.filter(container=container)
    if result:
        return result[0]
    else:
        print("make_title_content: {}".format(container.section.layout.name))
        return make_title_content(container, ModerateState.pending(), title)


def _init_content(container, company):
    """Create a main content section - if there isn't one already."""
    result = HoldingContent.objects.filter(container=container)
    if result:
        return result[0]
    else:
        print("make_holding_content: {}".format(container.section.layout.name))
        return make_holding_content(container, ModerateState.pending(), company)


def init_app_holding():
    default_moderate_state()
    # page
    home = init_page('Home', 0, is_home=True)
    # layout
    body = init_layout('Body')
    footer = init_layout('Footer')
    # sections
    content_section = init_section(home, body)
    footer_section = init_section(home, footer)
    # holding content
    holding_container = init_container(content_section, 1)
    _init_content(holding_container, 'Please edit this content...')
    # footer
    footer_container = init_container(footer_section, 1)
    _init_footer(footer_container, 'Please edit this footer...')
