# -*- encoding: utf-8 -*-
from django.conf.urls import (
    patterns,
    url,
)

from compose.views import (
    CodeSnippetCreateView,
    CodeSnippetListView,
    CodeSnippetUpdateView,
)


urlpatterns = patterns(
    '',
    url(regex=r'^code/snippet/$',
        view=CodeSnippetListView.as_view(),
        name='compose.code.snippet.list'
        ),
    url(regex=r'^code/snippet/create/$',
        view=CodeSnippetCreateView.as_view(),
        name='compose.code.snippet.create'
        ),
    url(regex=r'^code/snippet/(?P<slug>[-\w\d]+)/edit/$',
        view=CodeSnippetUpdateView.as_view(),
        name='compose.code.snippet.update'
        ),
)
