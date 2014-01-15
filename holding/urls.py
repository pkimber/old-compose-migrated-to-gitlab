from django.conf.urls import (
    patterns,
    url,
)

from .views import (
    HoldingContentPublishView,
    HoldingContentUpdateView,
    PageDesignView,
    PageView,
    TitleContentPublishView,
    TitleContentUpdateView,
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
        view=HoldingContentPublishView.as_view(),
        name='holding.content.publish'
        ),
    url(regex=r'^content/(?P<pk>\d+)/edit/$',
        view=HoldingContentUpdateView.as_view(),
        name='holding.content.update'
        ),
    url(regex=r'^title/(?P<pk>\d+)/publish/$',
        view=TitleContentPublishView.as_view(),
        name='holding.title.publish'
        ),
    url(regex=r'^title/(?P<pk>\d+)/edit/$',
        view=TitleContentUpdateView.as_view(),
        name='holding.title.update'
        ),
)
