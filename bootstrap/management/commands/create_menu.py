# -*- encoding: utf-8 -*-
from django.core.management.base import BaseCommand

from block.models import (
    Link,
    Menu,
    MenuItem,
    Page,
    PageSection,
    Section,
    Template,
    Url,
)

class Command(BaseCommand):

    help = "create a menu for example_compose app"

    def create_page(self, slug, title, template, sections):
        page = Page.objects.init_page(
            slug,
            '',
            title,
            0,
            template,
        )

        for section in sections:
            PageSection.objects.init_page_section(page, section)

        return page



    def handle(self, *args, **options):
        print ("Creating pages...")
        Template.objects.init_template('compose/page_article.html')
        Template.objects.init_template('compose/page_feature.html')
        section_body = Section.objects.get(slug='body')
        section_header = Section.objects.init_section(
            'header',
            'HEADER',
            'compose',
            'Header',
            'compose.header.create',
        )
        section_feature = Section.objects.init_section(
            'feature',
            'FEATURE',
            'compose',
            'Feature',
            'compose.feature.create',
        )

        page_article = self.create_page(
            'article-demo',
            'Article Demo',
            'compose/page_article.html',
            [ section_body ]
        )

        page_another = self.create_page(
            'another-page',
            'Another Page',
            'compose/page_article.html',
            [ section_body ]
        )

        page_feature = self.create_page(
            'feature-demo',
            'Feature Demo',
            'compose/page_feature.html',
            [ section_header, section_feature ]
        )

        page_header = self.create_page(
            'header-demo',
            'Header Demo',
            'compose/page_feature.html',
            [ section_header, section_feature ]
        )

        page_first = self.create_page(
            'first-page',
            'First page',
            'compose/page_article.html',
            [ section_body ]
        )

        print("Creating menu...")
        menu = Menu(slug='main', title='Main', navigation=True)
        menu.save()
        """
        feature_link = Link(title='Feature Demo', url='/feature-demo/', page=page_feature)
        feature_link.save()
        header_link = Link(title='Header Demo', url='/header-demo/', page=page_header)
        header_link.save()
        article_link = Link(title='Article Demo', url='/article-demo/', page=page_article)
        article_link.save()
        another_link = Link(title='Another Page', url='/another-page/', page=page_another)
        another_link.save()

        dash_link = Link(title='Dashboard', url='/home/user/')
        dash_link.save()

        first_link = Link(title='First Page', url='/first-page/', page=page_first)
        first_link.save()
        """

        Url.objects.init_pages()

        feature_link = Link.objects.create_internal_link(
            Url.objects.get(page=page_feature)
        )
        article_link = Link.objects.create_internal_link(
            Url.objects.get(page=page_article)
        )
        header_link = Link.objects.create_internal_link(
            Url.objects.get(page=page_header)
        )
        first_link = Link.objects.create_internal_link(
            Url.objects.get(page=page_first)
        )
        another_link = Link.objects.create_internal_link(
            Url.objects.get(page=page_another)
        )

        dash_url = Url.objects.init_reverse_url('Dashboard', 'project.dash')
        dash_link = Link.objects.create_internal_link(dash_url)

        menu_item = MenuItem(menu=menu, slug='demos', title='Demos', order=2)
        menu_item.save()
        sub_menu_item = MenuItem(
            menu=menu, slug='feature-demo', parent=menu_item,
            title='Feature Demo', order=1, link=feature_link
        )
        sub_menu_item.save()
        sub_menu_item = MenuItem(
            menu=menu, slug='header-demo', parent=menu_item,
            title='Header Demo', order=2, link=header_link
        )
        sub_menu_item.save()
        sub_menu_item = MenuItem(
            menu=menu, slug='article-demo', parent=menu_item,
            title='Article Demo', order=3, link=article_link
        )
        sub_menu_item.save()

        menu_item = MenuItem(menu=menu, slug='another-page',
            title='Another Page', order=3, link=another_link
        )
        menu_item.save()
        menu_item = MenuItem(menu=menu, slug='first-page',
            title='First Page', order=1, link=first_link
        )
        menu_item.save()

        menu_item = MenuItem(menu=menu, slug='dashboard',
            title='Dashboard', order=9, link=dash_link
        )
        menu_item.save()
        print("Menu created")
