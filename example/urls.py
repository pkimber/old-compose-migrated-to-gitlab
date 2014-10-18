# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import (
    include,
    patterns,
    url,
)
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

from block.models import PAGE_HOME
from block.views import (
    PageDesignView,
    PageView,
)


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(regex=r'^',
        view=include('login.urls')
        ),
    url(regex=r'^admin/',
        view=include(admin.site.urls)
        ),
    url(r'^home/user/$',
        view=RedirectView.as_view(url=reverse_lazy('cms.page.list')),
        name='project.dash'
        ),
    url(regex=r'^cms/',
        view=include('cms.urls')
        ),
    url(regex=r'^compose/',
        view=include('compose.urls')
        ),
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
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#   ^ helper function to return a URL pattern for serving files in debug mode.
# https://docs.djangoproject.com/en/1.5/howto/static-files/#serving-files-uploaded-by-a-user

urlpatterns += staticfiles_urlpatterns()
