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
    TemplateListView,
    TemplateCreateView,
    TemplateUpdateView,
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
    url(regex=r'^template/$',
        view=TemplateListView.as_view(),
        name='cms.template.list'
        ),
    url(regex=r'^template/create/$',
        view=TemplateCreateView.as_view(),
        name='cms.template.create'
        ),
    url(regex=r'^template/(?P<pk>\d+)/update/$',
        view=TemplateUpdateView.as_view(),
        name='cms.template.update'
        ),
)
