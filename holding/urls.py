from django.conf.urls import (
    patterns,
    url,
)

from .views import (
    PageDesignView,
    PageView,
)


urlpatterns = patterns(
    '',
    url(regex=r'^$',
        view=PageView.as_view(),
        kwargs=dict(page='home'),
        name='project.home'
        ),
    url(regex=r'^design/',
        view=PageDesignView.as_view(),
        kwargs=dict(page='home'),
        name='project.page.design.home'
        ),
)
