# -*- encoding: utf-8 -*-
from block.models import (
    BlockError,
    Page,
    PageSection,
    Section,
    Template,
    TemplateSection,
    Url,
)
from compose.models import (
    Article,
    ArticleBlock,
    Feature,
    FeatureBlock,
    SECTION_BODY,
    SECTION_CARD,
    SECTION_GALLERY,
    SECTION_SLIDESHOW,
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
    return Page.objects.get(slug=Page.HOME)


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


def init_app_compose():
    # section - body
    body = Section.objects.init_section(
        SECTION_BODY,
        SECTION_BODY.capitalize(),
        'compose',
        'Article',
        'compose.article.create',
    )
    # section - card
    card = Section.objects.init_section(
        SECTION_CARD,
        SECTION_CARD.capitalize(),
        'compose',
        'Feature',
        'compose.feature.create',
    )
    # section - gallery
    gallery = Section.objects.init_section(
        SECTION_GALLERY,
        SECTION_GALLERY.capitalize(),
        'compose',
        'Slideshow',
        'compose.slideshow.create',
    )
    # section - slideshow
    slideshow = Section.objects.init_section(
        SECTION_SLIDESHOW,
        SECTION_SLIDESHOW.capitalize(),
        'compose',
        'Slideshow',
        'compose.slideshow.create',
    )
    # template - article
    article_template = Template.objects.init_template('Article', 'compose/page_article.html')
    TemplateSection.objects.init_template_section(article_template, body)
    TemplateSection.objects.init_template_section(article_template, card)
    TemplateSection.objects.init_template_section(article_template, slideshow)
    # template - gallery
    gallery_template = Template.objects.init_template('Gallery', 'compose/page_gallery.html')
    TemplateSection.objects.init_template_section(gallery_template, gallery)
    TemplateSection.objects.init_template_section(gallery_template, slideshow)
    # page - home
    home = Page.objects.init_page(
        Page.HOME,
        '',
        'Home',
        0,
        article_template,
        is_home=True,
    )
    # page - gallery - hidden on init
    page_gallery = Page.objects.init_page(
        'gallery',
        '',
        'Gallery',
        0,
        gallery_template,
    )
    PageSection.objects.init_page_section(home, body)
    PageSection.objects.init_page_section(home, card)
    PageSection.objects.init_page_section(home, slideshow)
    PageSection.objects.init_page_section(page_gallery, gallery)
    PageSection.objects.init_page_section(page_gallery, slideshow)
    # Link wizard
    Url.objects.init_pages()
