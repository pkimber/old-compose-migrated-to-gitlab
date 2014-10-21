# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from base.form_utils import RequiredFieldForm
from block.models import (
    Page,
    Section,
)

from .models import (
    HeaderFooter,
    Template,
    TemplateSection,
)


class HeaderFooterForm(RequiredFieldForm):

    def __init__(self, *args, **kwargs):
        super(HeaderFooterForm, self).__init__(*args, **kwargs)
        self.fields['header'].widget.attrs.update(
            {'class': 'pure-input-2-3'}
        )

    class Meta:
        model = HeaderFooter
        fields = (
            'header',
            'footer_left',
            'footer_right',
        )


class PageForm(RequiredFieldForm):

    template = forms.ModelChoiceField(Template.objects.all())

    class Meta:
        model = Page
        fields = (
            'name',
            'slug',
            'slug_menu',
            'order',
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
