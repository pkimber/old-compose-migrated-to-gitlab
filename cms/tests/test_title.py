# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from block.tests.helper import check_content

from cms.tests.factories import TitleFactory


class TestTitle(TestCase):

    def test_content_methods(self):
        c = TitleFactory()
        check_content(c, ignore_remove=True)
