from django import forms

from base.form_utils import RequiredFieldForm

from .models import (
    HoldingContent,
    TitleContent,
)


class HoldingContentEmptyForm(forms.ModelForm):

    class Meta:
        model = HoldingContent
        fields = ()


class HoldingContentForm(RequiredFieldForm):

    def __init__(self, *args, **kwargs):
        super(HoldingContentForm, self).__init__(*args, **kwargs)
        for name in ('company', 'what_we_do', 'description'):
            self.fields[name].widget.attrs.update(
                {'class': 'pure-input-2-3'}
            )
        self.fields['company'].widget.attrs.update({
            'rows': '1',
        })

    class Meta:
        model = HoldingContent
        fields = (
            'company',
            'what_we_do',
            'description',
            'logo',
        )


class TitleContentEmptyForm(forms.ModelForm):

    class Meta:
        model = TitleContent
        fields = ()


class TitleContentForm(RequiredFieldForm):

    def __init__(self, *args, **kwargs):
        super(TitleContentForm, self).__init__(*args, **kwargs)
        for name in ('title',):
            self.fields[name].widget.attrs.update(
                {'class': 'pure-input-2-3'}
            )

    class Meta:
        model = TitleContent
        fields = (
            'title',
        )
