# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import (
    patterns,
    url,
)

from .views import (
    HoldingPublishView,
    HoldingUpdateView,
    PageDesignView,
    PageView,
    TitlePublishView,
    TitleUpdateView,
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
        name='holding.page.design.home'
        ),
    url(regex=r'^(?P<page>[-\w\d]+)/design/$',
        view=PageDesignView.as_view(),
        name='project.page.design'
        ),
    url(regex=r'^content/(?P<pk>\d+)/publish/$',
        view=HoldingPublishView.as_view(),
        name='holding.content.publish'
        ),
    url(regex=r'^content/(?P<pk>\d+)/edit/$',
        view=HoldingUpdateView.as_view(),
        name='holding.content.update'
        ),
    url(regex=r'^title/(?P<pk>\d+)/publish/$',
        view=TitlePublishView.as_view(),
        name='holding.title.publish'
        ),
    url(regex=r'^title/(?P<pk>\d+)/edit/$',
        view=TitleUpdateView.as_view(),
        name='holding.title.update'
        ),
)
