# -*- encoding: utf-8 -*-
from django.conf.urls import (
    patterns,
    url,
)

from compose.views import (
    # Article
    ArticleCreateView,
    ArticlePublishView,
    ArticleRemoveView,
    ArticleUpdateView,
    SlideshowCreateView,
    SlideshowPublishView,
    SlideshowRemoveView,
    SlideshowUpdateView,
    # Feature
    FeatureCreateView,
    FeaturePublishView,
    FeatureRemoveView,
    FeatureUpdateView,
    # Header
    HeaderCreateView,
    HeaderPublishView,
    HeaderRemoveView,
    HeaderUpdateView,
    # Styles
    FeatureStyleCreateView,
    FeatureStyleListView,
    FeatureStyleUpdateView,
    HeaderStyleCreateView,
    HeaderStyleListView,
    HeaderStyleUpdateView,
)


urlpatterns = patterns(
    '',
    url(regex=r'^article/create/(?P<page>[-\w\d]+)/(?P<section>[-\w\d]+)/$',
        view=ArticleCreateView.as_view(),
        name='compose.article.create'
        ),
    url(regex=r'^article/create/(?P<page>[-\w\d]+)/(?P<menu>[-\w\d]+)/(?P<section>[-\w\d]+)/$',
        view=ArticleCreateView.as_view(),
        name='compose.article.create'
        ),
    url(regex=r'^article/(?P<pk>\d+)/publish/$',
        view=ArticlePublishView.as_view(),
        name='compose.article.publish'
        ),
    url(regex=r'^article/(?P<pk>\d+)/remove/$',
        view=ArticleRemoveView.as_view(),
        name='compose.article.remove'
        ),
    url(regex=r'^article/(?P<pk>\d+)/update/$',
        view=ArticleUpdateView.as_view(),
        name='compose.article.update'
        ),
    url(regex=r'^slideshow/create/(?P<page>[-\w\d]+)/(?P<section>[-\w\d]+)/$',
        view=SlideshowCreateView.as_view(),
        name='compose.slideshow.create'
        ),
    url(regex=r'^slideshow/create/(?P<page>[-\w\d]+)/(?P<menu>[-\w\d]+)/(?P<section>[-\w\d]+)/$',
        view=SlideshowCreateView.as_view(),
        name='compose.slideshow.create'
        ),
    url(regex=r'^slideshow/(?P<pk>\d+)/publish/$',
        view=SlideshowPublishView.as_view(),
        name='compose.slideshow.publish'
        ),
    url(regex=r'^slideshow/(?P<pk>\d+)/remove/$',
        view=SlideshowRemoveView.as_view(),
        name='compose.slideshow.remove'
        ),
    url(regex=r'^slideshow/(?P<pk>\d+)/update/$',
        view=SlideshowUpdateView.as_view(),
        name='compose.slideshow.update'
        ),
    # Feature
    url(regex=r'^feature/create/(?P<page>[-\w\d]+)/(?P<menu>[-\w\d]+)/(?P<section>[-\w\d]+)/$',
        view=FeatureCreateView.as_view(),
        name='compose.feature.create'
        ),
    url(regex=r'^feature/create/(?P<page>[-\w\d]+)/(?P<section>[-\w\d]+)/$',
        view=FeatureCreateView.as_view(),
        name='compose.feature.create'
        ),
    url(regex=r'^feature/(?P<pk>\d+)/publish/$',
        view=FeaturePublishView.as_view(),
        name='compose.feature.publish'
        ),
    url(regex=r'^feature/(?P<pk>\d+)/remove/$',
        view=FeatureRemoveView.as_view(),
        name='compose.feature.remove'
        ),
    url(regex=r'^feature/(?P<pk>\d+)/edit/$',
        view=FeatureUpdateView.as_view(),
        name='compose.feature.update'
        ),
    # Header
    url(regex=r'^header/create/(?P<page>[-\w\d]+)/(?P<section>[-\w\d]+)/$',
        view=HeaderCreateView.as_view(),
        name='compose.header.create'
        ),
    url(regex=r'^header/create/(?P<page>[-\w\d]+)/(?P<menu>[-\w\d]+)/(?P<section>[-\w\d]+)/$',
        view=HeaderCreateView.as_view(),
        name='compose.header.create'
        ),
    url(regex=r'^header/(?P<pk>\d+)/publish/$',
        view=HeaderPublishView.as_view(),
        name='compose.header.publish'
        ),
    url(regex=r'^header/(?P<pk>\d+)/remove/$',
        view=HeaderRemoveView.as_view(),
        name='compose.header.remove'
        ),
    url(regex=r'^header/(?P<pk>\d+)/edit/$',
        view=HeaderUpdateView.as_view(),
        name='compose.header.update'
        ),
    # styles
    url(regex=r'^feature/style/create/$',
        view=FeatureStyleCreateView.as_view(),
        name='compose.feature.style.create'
        ),
    url(regex=r'^feature/style/list/$', 
        view=FeatureStyleListView.as_view(),
        name='compose.feature.style.list'
        ),
    url(regex=r'^feature/style/(?P<pk>\d+)/update/$',
        view=FeatureStyleUpdateView.as_view(),
        name='compose.feature.style.update'
        ),
    url(regex=r'^header/style/create/$',
        view=HeaderStyleCreateView.as_view(),
        name='compose.header.style.create'
        ),
    url(regex=r'^header/style/list/$', 
        view=HeaderStyleListView.as_view(),
        name='compose.header.style.list'
        ),
    url(regex=r'^header/style/(?P<pk>\d+)/update/$',
        view=HeaderStyleUpdateView.as_view(),
        name='compose.header.style.update'
        ),
)
