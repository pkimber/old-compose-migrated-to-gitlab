from django import forms

from base.form_utils import RequiredFieldForm

from .models import (
    HoldingContent,
    TitleContent,
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
