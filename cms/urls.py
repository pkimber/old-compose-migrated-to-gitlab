# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import (
    patterns,
    url,
)

from .views import (
    PageCreateView,
    PageListView,
    PageUpdateView,
)


urlpatterns = patterns(
    '',
    url(regex=r'^page/$',
        view=PageListView.as_view(),
        name='cms.page.list'
        ),
    url(regex=r'^page/create/$',
        view=PageCreateView.as_view(),
        name='cms.page.create'
        ),
    url(regex=r'^page/(?P<pk>\d+)/update/$',
        view=PageUpdateView.as_view(),
        name='cms.page.update'
        ),
)
