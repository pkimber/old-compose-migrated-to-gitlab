# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from base.tests.test_utils import PermTestCase

from block.tests.factories import PageFactory

from holding.tests.factories import (
    HoldingFactory,
    TitleFactory,
)


class TestViewPerm(PermTestCase):

    def setUp(self):
        self.setup_users()

    def test_content_publish(self):
        c = HoldingFactory()
        url = reverse('holding.content.publish', kwargs={'pk': c.pk})
        self.assert_staff_only(url)

    def test_content_update(self):
        c = HoldingFactory()
        url = reverse('holding.content.update', kwargs={'pk': c.pk})
        self.assert_staff_only(url)

    def test_footer_publish(self):
        c = TitleFactory()
        url = reverse('holding.title.publish', kwargs={'pk': c.pk})
        self.assert_staff_only(url)

    def test_footer_update(self):
        c = TitleFactory()
        url = reverse('holding.title.update', kwargs={'pk': c.pk})
        self.assert_staff_only(url)

    def test_home(self):
        PageFactory(
            slug='home', slug_menu='',
            template_name='holding/page_content.html',
        )
        url = reverse('project.home')
        self.assert_any(url)

    def test_page_design_home(self):
        p = PageFactory(
            slug='home', slug_menu='',
            template_name='holding/page_content.html',
        )
        url = reverse('project.page.design', kwargs=dict(page=p.slug))
        self.assert_staff_only(url)
