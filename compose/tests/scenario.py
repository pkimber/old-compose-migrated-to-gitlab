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
    FeatureStyle,
    Header,
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
    # section - header
    header_a = Section.objects.init_section(
        Header.SECTION_A,
        Header.SECTION_A.capitalize(),
        'compose',
        'Header',
        'compose.header.create',
    )
    # section - feature
    feature_a = Section.objects.init_section(
        Feature.SECTION_A,
        Feature.SECTION_A.capitalize(),
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
    # template - feature
    feature_template = Template.objects.init_template('Gallery', 'compose/page_feature.html')
    TemplateSection.objects.init_template_section(feature_template, header_a)
    TemplateSection.objects.init_template_section(feature_template, feature_a)
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
    # page - features - hidden on init
    page_feature = Page.objects.init_page(
        'feature',
        '',
        'Feature',
        0,
        feature_template,
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
    PageSection.objects.init_page_section(page_feature, header_a)
    PageSection.objects.init_page_section(page_feature, feature_a)
    PageSection.objects.init_page_section(page_gallery, gallery)
    PageSection.objects.init_page_section(page_gallery, slideshow)

    FeatureStyle.objects.get_or_create(name='card', css_class_name='card')
    FeatureStyle.objects.get_or_create(name='jumbotron', css_class_name='jumbotron')
    FeatureStyle.objects.get_or_create(name='card-light-img-overlay', css_class_name='card img-overlay')
    FeatureStyle.objects.get_or_create(name='card-dark-img-overlay', css_class_name='card card-inverse')
    FeatureStyle.objects.get_or_create(name='card-primary', css_class_name='card card-inverse card-primary')
    FeatureStyle.objects.get_or_create(name='card-secondary', css_class_name='card card-inverse card-secondary')
    FeatureStyle.objects.get_or_create(name='card-info', css_class_name='card card-inverse card-info')
    FeatureStyle.objects.get_or_create(name='card-warning', css_class_name='card card-inverse card-warning')
    FeatureStyle.objects.get_or_create(name='card-danger', css_class_name='card card-inverse card-danger')


    # Link wizard
    Url.objects.init_pages()
