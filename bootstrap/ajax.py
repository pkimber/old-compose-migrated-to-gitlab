# -*- encoding: utf-8 -*-
from django_ajax.decorators import ajax
from django.core.urlresolvers import reverse
from bootstrap.models import *

@ajax
def toggle_map(request):
    error = False
    error_msg = ''
    ft = PageFooter.load()
    ft.show_map = not ft.show_map
    ft.save()
    # TODO remove
    data = {}
    if ft.show_map:
        data['reload'] = True
    else:
        data['remove'] = {}
        data['inner-fragments'] = {}
        data['remove']['.ajxobj_map_row'] = not ft.show_map
        data['inner-fragments'] = {}
        data['inner-fragments']['.ajxobj_map_button'] = '{} Map'.format(
                                        'Hide' if ft.show_map else 'Show')
    return data
