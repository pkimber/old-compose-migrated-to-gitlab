# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.test import TestCase

from block.tests.scenario import default_moderate_state
from login.tests.scenario import (
    default_scenario_login,
    get_user_staff,
    STAFF,
)

from holding.tests.scenario import (
    get_holding_content,
    get_title_content,
    init_app_holding,
)


class TestView(TestCase):

    def setUp(self):
        default_moderate_state()
        init_app_holding()
        default_scenario_login()
        staff = get_user_staff()
        self.assertTrue(
            self.client.login(username=staff.username, password=STAFF)
        )

    def test_publish_content(self):
        c = get_holding_content()
        response = self.client.post(
            reverse('holding.content.publish', kwargs={'pk': c.pk}),
        )
        self.assertEqual(response.status_code, 302)

    def test_publish_footer(self):
        c = get_title_content()
        response = self.client.post(
            reverse('holding.title.publish', kwargs={'pk': c.pk}),
        )
        self.assertEqual(response.status_code, 302)

    def test_update_content(self):
        c = get_holding_content()
        response = self.client.post(
            reverse('holding.content.update', kwargs={'pk': c.pk}),
            {'company': 'pkimber.net'}
        )
        self.assertEqual(response.status_code, 302)

    def test_update_footer(self):
        c = get_title_content()
        response = self.client.post(
            reverse('holding.title.update', kwargs={'pk': c.pk}),
            {'title': 'Hatherleigh'}
        )
        self.assertEqual(response.status_code, 302)
