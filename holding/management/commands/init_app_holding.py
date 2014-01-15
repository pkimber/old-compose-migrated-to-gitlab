from django.core.management.base import BaseCommand

from cms.models import ModerateState
from cms.service import (
    init_container,
    init_layout,
    init_page,
    init_section,
)
from cms.tests.scenario import default_moderate_state
from holding.models import TitleContent
from holding.tests.model_maker import make_title_content


class Command(BaseCommand):

    help = "Initialise 'holding' application"

    def _init_footer(self, container, title):
        """Create a footer - if there isn't one already."""
        result = TitleContent.objects.filter(container=container)
        if result:
            return result[0]
        else:
            print("make_title_content: {}".format(container.section.layout.name))
            return make_title_content(container, ModerateState.pending(), title)

    def handle(self, *args, **options):
        default_moderate_state()
        # page
        home = init_page('Home', 0, is_home=True)
        # layout
        body = init_layout('Body')
        footer = init_layout('Footer')
        # sections
        init_section(home, body)
        footer_section = init_section(home, footer)
        # footer
        footer_container = init_container(footer_section, 1)
        self._init_footer(
            footer_container,
            'Please edit this footer...'
        )
        print "Initialised 'holding' app..."
