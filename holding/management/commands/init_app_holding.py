from django.core.management.base import BaseCommand

from holding.tests.scenario import init_app_holding


class Command(BaseCommand):

    help = "Initialise 'holding' application"

    def handle(self, *args, **options):
        init_app_holding()
        print "Initialised 'holding' app..."
