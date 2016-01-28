# -*- encoding: utf-8 -*-
from django.test import TestCase

from compose.management.commands import (
    demo_data_compose,
    init_app_compose,
    init_app_compose_news,
)


class TestCommand(TestCase):

    def test_demo_data(self):
        """ Test the management command """
        command = demo_data_compose.Command()
        command.handle()

    def test_init_app(self):
        """ Test the management command """
        command = init_app_compose.Command()
        command.handle()

    def test_init_app_news(self):
        """ Test the management command """
        command = init_app_compose.Command()
        command.handle()
        command = init_app_compose_news.Command()
        command.handle()
