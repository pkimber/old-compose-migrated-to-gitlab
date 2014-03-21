# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from block.models import ModerateState
from block.tests.helper import check_content_methods
from block.tests.model_maker import (
    make_page,
    make_section,
)
from block.tests.scenario import default_moderate_state
from login.tests.scenario import default_scenario_login

from holding.tests.scenario import (
    get_holding_content,
    init_app_holding,
)


class TestHolding(TestCase):

    def setUp(self):
        default_moderate_state()
        init_app_holding()

    def test_content_methods(self):
        c = get_holding_content()
        check_content_methods(c, ignore_remove=True)
