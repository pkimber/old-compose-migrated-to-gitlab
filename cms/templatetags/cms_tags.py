# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django import template

from block.models import Page

register = template.Library()


@register.inclusion_tag('cms/_menu.html', takes_context=True)
def cms_menu(context):
    return dict(
        design=context.get('design', False),
        is_block_page=context.get('is_block_page', False),
        page=context.get('page', None),
        pages=Page.objects.menu(),
        user=context.get('user', None),
    )
