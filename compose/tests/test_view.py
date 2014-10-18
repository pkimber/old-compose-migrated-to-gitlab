# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.test import TestCase

from login.tests.factories import (
    TEST_PASSWORD,
    UserFactory,
)

from compose.tests.factories import (
    HoldingFactory,
    TitleFactory,
)


class TestView(TestCase):

    def setUp(self):
        self.user = UserFactory(username='staff', is_staff=True)
        self.assertTrue(
            self.client.login(
                username=self.user.username,
                password=TEST_PASSWORD
            )
        )

    def test_publish_holding(self):
        c = HoldingFactory()
        response = self.client.post(
            reverse('compose.holding.publish', kwargs={'pk': c.pk}),
        )
        self.assertEqual(response.status_code, 302)

    def test_publish_footer(self):
        c = TitleFactory()
        response = self.client.post(
            reverse('compose.title.publish', kwargs={'pk': c.pk}),
        )
        self.assertEqual(response.status_code, 302)

    def test_update_holding(self):
        c = HoldingFactory()
        response = self.client.post(
            reverse('compose.holding.update', kwargs={'pk': c.pk}),
            {'company': 'pkimber.net'}
        )
        self.assertEqual(response.status_code, 302)

    def test_update_footer(self):
        c = TitleFactory()
        response = self.client.post(
            reverse('compose.title.update', kwargs={'pk': c.pk}),
            {'title': 'Hatherleigh'}
        )
        self.assertEqual(response.status_code, 302)
