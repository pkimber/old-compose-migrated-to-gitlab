# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from block.tests.helper import check_content

from compose.tests.factories import HoldingFactory


class TestHolding(TestCase):

    def test_content_methods(self):
        c = HoldingFactory()
        check_content(c, ignore_remove=True)
