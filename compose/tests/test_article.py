# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from block.tests.helper import check_content

from compose.tests.factories import ArticleFactory


class TestArticle(TestCase):

    def test_content_methods(self):
        c = ArticleFactory()
        check_content(c)
