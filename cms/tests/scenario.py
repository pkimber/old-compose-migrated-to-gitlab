# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from block.models import Page
from block.tests.scenario import init_app_block

from cms.models import (
    Template,
    TemplateSection,
)


def init_app_cms():
    init_app_block()
    # add existing templates and sections
    for page in Page.objects.pages():
        template = Template.objects.init_template(page.template_name)
        for page_section in page.pagesection_set.all():
            TemplateSection.objects.init_template_section(
                template,
                page_section.section,
            )
