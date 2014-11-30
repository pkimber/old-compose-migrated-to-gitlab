# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from block.models import (
    BlockError,
    Page,
    PAGE_HOME,
)
from block.service import (
    init_page,
    init_page_section,
    init_section,
)

from cms.models import (
    Template,
    TemplateSection,
)
from cms.tests.model_maker import (
    make_template,
    make_template_section,
)
from compose.models import (
    Article,
    ArticleBlock,
    SECTION_BODY,
)
from compose.tests.model_maker import (
    make_article,
    make_article_block,
)


def get_article_content():
    result = Article.objects.all()
    if result:
        return result[0]
    else:
        raise BlockError("Cannot find any article content")


def get_page_home():
    return Page.objects.get(slug=PAGE_HOME)


def _init_article(block, title):
    """Create a main content section - if there isn't one already."""
    result = Article.objects.filter(block=block)
    if result:
        return result[0]
    else:
        print("make_article: {}".format(title))
        return make_article(block, 1, title)


def _init_article_block(page_section):
    try:
        result = ArticleBlock.objects.get(page_section=page_section)
    except ArticleBlock.DoesNotExist:
        print("make_article_block: {}".format(page_section))
        result = make_article_block(page_section)
    return result


def _init_template(template_name):
    result = Template.objects.filter(template_name=template_name)
    if result:
        return result[0]
    else:
        print("make_template: {}".format(template_name))
        return make_template(template_name)


def _init_template_section(template, section):
    try:
        TemplateSection.objects.get(template=template, section=section)
    except TemplateSection.DoesNotExist:
        print("make_template_section: {}".format(template.template_name))
        return make_template_section(template, section)


def init_app_compose():
    # page
    # name, slug_page, order, template_name, is_home=None, slug_menu=None):
    home = init_page(
        'Home',
        PAGE_HOME,
        0,
        'compose/page_article.html',
        is_home=True,
    )
    # layout
    body = init_section(
        SECTION_BODY.capitalize(),
        'compose',
        'Article',
        'compose.article.create',
    )
    init_page_section(home, body)
    # template
    template = _init_template('compose/page_article.html')
    _init_template_section(template, body)
