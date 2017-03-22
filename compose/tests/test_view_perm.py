# -*- encoding: utf-8 -*-
from django.core.urlresolvers import reverse

from base.tests.test_utils import PermTestCase, assert_redirect

from block.tests.factories import (
    PageFactory,
    PageSectionFactory,
    TemplateFactory,
)
from compose.tests.factories import (
    ArticleFactory,
    CodeSnippetFactory,
    SidebarFactory,
    SlideshowFactory,
)


class TestViewPerm(PermTestCase):

    def setUp(self):
        self.setup_users()

    def test_article_create(self):
        p = PageSectionFactory()
        url = reverse(
            'compose.article.create',
            kwargs=dict(
                page=p.page.slug,
                menu=p.page.slug_menu,
                section=p.section.slug,
            )
        )
        self.assert_staff_only(url)

    def test_article_publish(self):
        c = ArticleFactory()
        url = reverse('compose.article.publish', kwargs={'pk': c.pk})
        self.assert_staff_only(url)

    def test_article_remove(self):
        c = ArticleFactory()
        url = reverse('compose.article.remove', kwargs={'pk': c.pk})
        self.assert_staff_only(url)

    def test_article_update(self):
        c = ArticleFactory()
        url = reverse('compose.article.update', kwargs={'pk': c.pk})
        self.assert_staff_only(url)

    def test_article_up(self):
        c = ArticleFactory()
        url = reverse('compose.article.up', kwargs={'pk': c.pk})
        self.client.logout()
        response = self.client.get(url)
        assert_redirect(response, 'login')
        staff = self.login_staff()
        response = self.client.get(url)
        assert_redirect(response, 'design')

    def test_article_down(self):
        c = ArticleFactory()
        url = reverse('compose.article.down', kwargs={'pk': c.pk})
        self.client.logout()
        response = self.client.get(url)
        assert_redirect(response, 'login')
        staff = self.login_staff()
        response = self.client.get(url)
        assert_redirect(response, 'design')

    def test_code_snippet_list(self):
        url = reverse('compose.code.snippet.list')
        self.assert_staff_only(url)

    def test_code_snippet_create(self):
        url = reverse('compose.code.snippet.create')
        self.assert_staff_only(url)

    def test_code_snippet_update(self):
        snippet = CodeSnippetFactory()
        url = reverse('compose.code.snippet.update', args=[snippet.slug])
        self.assert_staff_only(url)

    def test_home(self):
        template = TemplateFactory(template_name='compose/page_article.html')
        PageFactory(is_home=True, slug='home', slug_menu='', template=template)
        url = reverse('project.home')
        self.assert_any(url)

    def test_page_design_home(self):
        template = TemplateFactory(template_name='compose/page_article.html')
        p = PageFactory(slug='home', slug_menu='', template=template)
        url = reverse('project.page.design', kwargs=dict(page=p.slug))
        self.assert_staff_only(url)

    def test_sidebar_create(self):
        p = PageSectionFactory()
        url = reverse(
            'compose.sidebar.create',
            kwargs=dict(
                page=p.page.slug,
                menu=p.page.slug_menu,
                section=p.section.slug,
            )
        )
        self.assert_staff_only(url)

    def test_sidebar_publish(self):
        c = SidebarFactory()
        url = reverse('compose.sidebar.publish', kwargs={'pk': c.pk})
        self.assert_staff_only(url)

    def test_sidebar_remove(self):
        c = SidebarFactory()
        url = reverse('compose.sidebar.remove', kwargs={'pk': c.pk})
        self.assert_staff_only(url)

    def test_sidebar_update(self):
        c = SidebarFactory()
        url = reverse('compose.sidebar.update', kwargs={'pk': c.pk})
        self.assert_staff_only(url)

    def test_slideshow_create(self):
        p = PageSectionFactory()
        url = reverse(
            'compose.slideshow.create',
            kwargs=dict(
                page=p.page.slug,
                menu=p.page.slug_menu,
                section=p.section.slug,
            )
        )
        self.assert_staff_only(url)

    def test_slideshow_publish(self):
        c = SlideshowFactory()
        url = reverse('compose.slideshow.publish', kwargs={'pk': c.pk})
        self.assert_staff_only(url)

    def test_slideshow_remove(self):
        c = SlideshowFactory()
        url = reverse('compose.slideshow.remove', kwargs={'pk': c.pk})
        self.assert_staff_only(url)

    def test_slideshow_update(self):
        c = SlideshowFactory()
        url = reverse('compose.slideshow.update', kwargs={'pk': c.pk})
        self.assert_staff_only(url)
