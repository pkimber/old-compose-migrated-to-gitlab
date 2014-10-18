# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from base.form_utils import RequiredFieldForm
from block.models import Page


class PageForm(RequiredFieldForm):

    class Meta:
        model = Page
        fields = (
            'name',
            'slug',
            'slug_menu',
            'order',
            'is_home',
            'template_name',
            'deleted',
        )
