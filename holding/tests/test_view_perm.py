# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from base.tests.test_utils import PermTestCase
from block.tests.scenario import default_scenario_block
from login.tests.scenario import default_scenario_login

from holding.tests.scenario import (
    get_holding_content,
    get_page_home,
    get_title_content,
    init_app_holding,
)


class TestViewPerm(PermTestCase):

    def setUp(self):
        default_scenario_block()
        init_app_holding()
        default_scenario_login()

    def test_content_publish(self):
        content = get_holding_content()
        url = reverse('holding.content.publish', kwargs={'pk': content.pk})
        self.assert_staff_only(url)

    def test_content_update(self):
        content = get_holding_content()
        url = reverse('holding.content.update', kwargs={'pk': content.pk})
        self.assert_staff_only(url)

    def test_footer_publish(self):
        content = get_title_content()
        url = reverse('holding.title.publish', kwargs={'pk': content.pk})
        self.assert_staff_only(url)

    def test_footer_update(self):
        content = get_title_content()
        url = reverse('holding.title.update', kwargs={'pk': content.pk})
        self.assert_staff_only(url)

    def test_home(self):
        url = reverse('project.home')
        self.assert_any(url)

    def test_page_design_home(self):
        page = get_page_home()
        url = reverse('project.page.design', kwargs=dict(page=page.slug))
        self.assert_staff_only(url)
