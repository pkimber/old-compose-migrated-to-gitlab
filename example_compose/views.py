# -*- encoding: utf-8 -*-
from django.views.generic import TemplateView

from base.view_utils import BaseMixin


class SettingsView(BaseMixin, TemplateView):

    template_name = 'example/settings.html'
