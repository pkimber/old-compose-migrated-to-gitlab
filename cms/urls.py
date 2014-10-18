# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import (
    patterns,
    url,
)

from block.views import (
    PageDesignView,
    PageView,
)
from .models import PAGE_HOME
from .views import (
    HoldingPublishView,
    HoldingUpdateView,
    TitlePublishView,
    TitleUpdateView,
)


urlpatterns = patterns(
    '',
    url(regex=r'^$',
        view=PageView.as_view(),
        kwargs=dict(page=PAGE_HOME),
        name='project.home'
        ),
    url(regex=r'^(?P<page>[-\w\d]+)/design/$',
        view=PageDesignView.as_view(),
        name='project.page.design'
        ),
    url(regex=r'^(?P<page>[-\w\d]+)/(?P<menu>[-\w\d]+)/design/$',
        view=PageDesignView.as_view(),
        name='project.page.design'
        ),
    url(regex=r'^(?P<page>[-\w\d]+)/$',
        view=PageView.as_view(),
        name='project.page'
        ),
    url(regex=r'^(?P<page>[-\w\d]+)/(?P<menu>[-\w\d]+)/$',
        view=PageView.as_view(),
        name='project.page'
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
