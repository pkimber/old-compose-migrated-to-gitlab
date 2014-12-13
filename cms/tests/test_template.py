# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from block.tests.factories import PageFactory
from cms.tests.factories import (
    TemplateFactory,
    TemplateSectionFactory,
)


class TestTemplate(TestCase):

    def test_setup_page(self):
        """'setup_page' will update the pages with the new sections."""
        page = PageFactory()
        template = TemplateFactory(template_name=page.template_name)
        template_section = TemplateSectionFactory(template=template)
        self.assertEqual(0, page.pagesection_set.all().count())
        self.assertEqual(1, template.templatesection_set.all().count())
        template.setup_page(page)
        self.assertEqual(1, page.pagesection_set.all().count())
