# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from base.form_utils import RequiredFieldForm

from .models import Article


class ArticleEmptyForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ()


class ArticleForm(RequiredFieldForm):

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        for name in ('title', 'description'):
            self.fields[name].widget.attrs.update(
                {'class': 'pure-input-2-3'}
            )

    class Meta:
        model = Article
        fields = (
            'title',
            'description',
            'picture',
        )
        widgets = {
            'picture': forms.FileInput,
        }
