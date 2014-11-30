# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import (
    patterns,
    url,
)

from cms.views import (
    HeaderFooterUpdateView,
    PageCreateView,
    PageListView,
    PageUpdateView,
    SectionCreateView,
    SectionListView,
    SectionUpdateView,
    TemplateCreateView,
    TemplateListView,
    TemplateSectionCreateView,
    TemplateSectionRemoveView,
    TemplateUpdateView,
)


urlpatterns = patterns(
    '',
    url(regex=r'^header-footer/$',
        view=HeaderFooterUpdateView.as_view(),
        name='cms.header.footer.update'
        ),
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
    url(regex=r'^section/$',
        view=SectionListView.as_view(),
        name='cms.section.list'
        ),
    url(regex=r'^section/create/$',
        view=SectionCreateView.as_view(),
        name='cms.section.create'
        ),
    url(regex=r'^section/(?P<pk>\d+)/update/$',
        view=SectionUpdateView.as_view(),
        name='cms.section.update'
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
    url(regex=r'^template/(?P<pk>\d+)/section/create/$',
        view=TemplateSectionCreateView.as_view(),
        name='cms.template.section.create'
        ),
    url(regex=r'^template/section/(?P<pk>\d+)/remove/$',
        view=TemplateSectionRemoveView.as_view(),
        name='cms.template.section.remove'
        ),
)
