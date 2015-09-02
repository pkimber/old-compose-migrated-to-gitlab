# -*- encoding: utf-8 -*-
from django.core.management.base import BaseCommand

from compose.models import CodeSnippet


class Command(BaseCommand):

    help = "Initialise 'compose' demo data"

    def handle(self, *args, **options):
        snippet = 'body { color: purple; }'
        CodeSnippet.objects.create_code_snippet(CodeSnippet.CSS, snippet)
        self.stdout.write("Initialised 'compose' demo data...")
