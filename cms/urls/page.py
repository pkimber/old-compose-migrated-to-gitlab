# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import (
    patterns,
    url,
)

from cms.views import (
    CmsPageDesignView,
    CmsPageView,
)

from block.models import PAGE_HOME


urlpatterns = patterns(
    '',
    url(regex=r'^$',
        view=CmsPageView.as_view(),
        kwargs=dict(page=PAGE_HOME),
        name='project.home'
        ),
    url(regex=r'^(?P<page>[-\w\d]+)/design/$',
        view=CmsPageDesignView.as_view(),
        name='project.page.design'
        ),
    url(regex=r'^(?P<page>[-\w\d]+)/(?P<menu>[-\w\d]+)/design/$',
        view=CmsPageDesignView.as_view(),
        name='project.page.design'
        ),
    url(regex=r'^(?P<page>[-\w\d]+)/$',
        view=CmsPageView.as_view(),
        name='project.page'
        ),
    url(regex=r'^(?P<page>[-\w\d]+)/(?P<menu>[-\w\d]+)/$',
        view=CmsPageView.as_view(),
        name='project.page'
        ),
)
