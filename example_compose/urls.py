# -*- encoding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

from .views import (
    DashView,
    SettingsView,
)

admin.autodiscover()


urlpatterns = [
    url(regex=r'^',
        view=include('login.urls')
        ),
    url(regex=r'^admin/',
        view=include(admin.site.urls)
        ),
    url(r'^home/user/$',
        view=RedirectView.as_view(url=reverse_lazy('block.page.list'), permanent=False),
        name='project.dash'
        ),
    url(r'^dash/$',
        view=DashView.as_view(),
        name='project.dash'
        ),
    url(r'^settings/$',
        view=SettingsView.as_view(),
        name='project.settings'
        ),
    url(regex=r'^block/',
        view=include('block.urls.block')
        ),
    url(regex=r'^wizard/',
        view=include('block.urls.wizard')
        ),
    url(regex=r'^compose/',
        view=include('compose.urls.compose')
        ),
    url(regex=r'^snippet/',
        view=include('compose.urls.snippet')
        ),
    # this url include should come last
    url(regex=r'^',
        view=include('block.urls.cms')
        ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#   ^ helper function to return a URL pattern for serving files in debug mode.
# https://docs.djangoproject.com/en/1.5/howto/static-files/#serving-files-uploaded-by-a-user

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
