# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView

from base.view_utils import BaseMixin
from booking.models import BookingSettings


class SettingsView(BaseMixin, TemplateView):

    template_name = 'settings/home.html'

    def get_context_data(self, **kwargs):
        context = super(SettingsView, self).get_context_data(**kwargs)
        context.update(dict(
            booking_settings=BookingSettings.load(),
        ))
        return context
