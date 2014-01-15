from base.tests.model_maker import clean_and_save

from holding.models import TitleContent


def make_title_content(container, moderate_state, title, **kwargs):
    defaults = dict(
        container=container,
        moderate_state=moderate_state,
        title=title,
    )
    defaults.update(kwargs)
    return clean_and_save(TitleContent(**defaults))
