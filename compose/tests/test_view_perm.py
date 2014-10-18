# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from base.tests.test_utils import PermTestCase

from compose.tests.factories import (
    HoldingFactory,
    TitleFactory,
)


class TestViewPerm(PermTestCase):

    def setUp(self):
        self.setup_users()

    def test_content_publish(self):
        c = HoldingFactory()
        url = reverse('compose.holding.publish', kwargs={'pk': c.pk})
        self.assert_staff_only(url)

    def test_content_update(self):
        c = HoldingFactory()
        url = reverse('compose.holding.update', kwargs={'pk': c.pk})
        self.assert_staff_only(url)

    def test_footer_publish(self):
        c = TitleFactory()
        url = reverse('compose.title.publish', kwargs={'pk': c.pk})
        self.assert_staff_only(url)

    def test_footer_update(self):
        c = TitleFactory()
        url = reverse('compose.title.update', kwargs={'pk': c.pk})
        self.assert_staff_only(url)
