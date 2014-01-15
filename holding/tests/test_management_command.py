from django.test import TestCase

from holding.management.commands import init_app_holding


class TestCommand(TestCase):

    def test_init_app(self):
        """ Test the management command """
        command = init_app_holding.Command()
        command.handle()
