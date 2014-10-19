# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from base.tests.model_maker import clean_and_save

from cms.models import Template


def make_template(template_name, **kwargs):
    defaults = dict(
        template_name=template_name,
    )
    defaults.update(kwargs)
    return clean_and_save(Template(**defaults))
