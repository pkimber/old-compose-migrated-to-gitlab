# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from base.tests.test_utils import PermTestCase

from block.tests.factories import PageSectionFactory
from compose.tests.factories import ArticleFactory


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
