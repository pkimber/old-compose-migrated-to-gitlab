# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from base.form_utils import RequiredFieldForm

from .models import (
    Holding,
    Title,
)


class HoldingEmptyForm(forms.ModelForm):

    class Meta:
        model = Holding
        fields = ()


class HoldingForm(RequiredFieldForm):

    def __init__(self, *args, **kwargs):
        super(HoldingForm, self).__init__(*args, **kwargs)
        for name in ('company', 'what_we_do', 'description'):
            self.fields[name].widget.attrs.update(
                {'class': 'pure-input-2-3'}
            )
        self.fields['company'].widget.attrs.update({
            'rows': '1',
        })

    class Meta:
        model = Holding
        fields = (
            'company',
            'what_we_do',
            'description',
            'logo',
        )
        widgets = {
            'logo': forms.FileInput,
        }


class TitleEmptyForm(forms.ModelForm):

    class Meta:
        model = Title
        fields = ()


class TitleForm(RequiredFieldForm):

    def __init__(self, *args, **kwargs):
        super(TitleForm, self).__init__(*args, **kwargs)
        for name in ('title',):
            self.fields[name].widget.attrs.update(
                {'class': 'pure-input-2-3'}
            )

    class Meta:
        model = Title
        fields = (
            'title',
        )
