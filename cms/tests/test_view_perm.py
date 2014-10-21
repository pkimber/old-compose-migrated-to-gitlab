# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from base.tests.test_utils import PermTestCase

from block.tests.factories import PageFactory
from login.tests.factories import UserFactory


class TestViewPerm(PermTestCase):

    def setUp(self):
        UserFactory(username='staff', is_staff=True, is_superuser=True)
        UserFactory(username='web')

    def test_create(self):
        self.assert_staff_only(reverse('cms.page.create'))

    def test_header_footer_update(self):
        self.assert_staff_only(reverse('cms.header.footer.update'))

    def test_list(self):
        self.assert_staff_only(reverse('cms.page.list'))

    def test_update(self):
        page = PageFactory()
        self.assert_staff_only(
            reverse('cms.page.update', kwargs=dict(pk=page.pk))
        )

    def test_home(self):
        PageFactory(
            slug='home', slug_menu='',
            template_name='compose/page_content.html',
        )
        url = reverse('project.home')
        self.assert_any(url)

    def test_page_design_home(self):
        p = PageFactory(
            slug='home', slug_menu='',
            template_name='compose/page_content.html',
        )
        url = reverse('project.page.design', kwargs=dict(page=p.slug))
        self.assert_staff_only(url)
