# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from base.form_utils import RequiredFieldForm
from block.models import (
    Page,
    Section,
)

from .models import (
    Template,
    TemplateSection,
)


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


class SectionForm(RequiredFieldForm):

    class Meta:
        model = Section
        fields = (
            'name',
            'slug',
            'block_app',
            'block_model',
            'create_url_name',
            'paginated',
        )


class TemplateForm(RequiredFieldForm):

    class Meta:
        model = Template
        fields = (
            'template_name',
        )


class TemplateSectionEmptyForm(forms.ModelForm):

    class Meta:
        model = TemplateSection
        fields = ()


class TemplateSectionForm(RequiredFieldForm):

    class Meta:
        model = TemplateSection
        fields = (
            'section',
        )
