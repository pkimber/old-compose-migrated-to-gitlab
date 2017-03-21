# -*- encoding: utf-8 -*-
from django.views.generic import TemplateView

from base.view_utils import BaseMixin
from block.views import CmsPageView
from compose.models import CodeSnippet


class HomeView(CmsPageView):

    template_name = 'web/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            obj = CodeSnippet.objects.get(slug=CodeSnippet.CSS)
            snippet = obj.code
        except CodeSnippet.DoesNotExist:
            snippet = ''
        context.update(dict(snippet=snippet))
        return context


class DashView(BaseMixin, TemplateView):

    template_name = 'compose/dash.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            obj = CodeSnippet.objects.get(slug=CodeSnippet.CSS)
            snippet = obj.code
        except CodeSnippet.DoesNotExist:
            snippet = ''
        context.update(dict(snippet=snippet))
        return context


class DashView(BaseMixin, TemplateView):

    template_name = 'compose/dash.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            obj = CodeSnippet.objects.get(slug=CodeSnippet.CSS)
            snippet = obj.code
        except CodeSnippet.DoesNotExist:
            snippet = ''
        context.update(dict(snippet=snippet))
        return context


class SettingsView(BaseMixin, TemplateView):

    template_name = 'compose/settings.html'
