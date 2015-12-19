# -*- encoding: utf-8 -*-
from django.core.management.base import BaseCommand

from block.models import (
    Page,
    PageSection,
    PaginatedSection,
    Section,
    Template,
    TemplateSection,
)
from compose.models import SECTION_NEWS
from compose.tests.scenario import init_app_compose


class Command(BaseCommand):

    help = "Initialise 'compose' application... add news section..."

    def handle(self, *args, **options):
        # section - news
        paginated = PaginatedSection.objects.init_paginated_section(3, '-created')
        news = Section.objects.init_section(
            SECTION_NEWS,
            SECTION_NEWS.capitalize(),
            'compose',
            'Article',
            'compose.article.create',
            paginated=paginated,
        )
        template = Template.objects.get(
            template_name='compose/page_article.html'
        )
        TemplateSection.objects.init_template_section(template, news)
        home = Page.objects.get(slug=Page.HOME, slug_menu='')
        PageSection.objects.init_page_section(home, news)
        print("Initialised 'compose' app... add news section...")
