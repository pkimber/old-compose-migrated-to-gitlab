# -*- encoding: utf-8 -*-
from django import template

register = template.Library()

# @register.inclusion_tag('bootstrap/_cms_inctag_pagination_button.html')
# def cms_pagination_button(cur_page_no, target_page_jump, page_max):
#     return dict(
#         cur_page_no=cur_page_no,
#         target_page_jump=target_page_jump,
#         page_max=page_max,
#     )
#
#
# @register.inclusion_tag('bootstrap/_cms_inctag_moderate.html')
# def cms_moderate(generic_content, can_remove=True, caption='',
#         is_first=False, is_last=False, can_reorder=True, return_path=None):
#     return dict(
#                 c=generic_content,
#                 can_remove=can_remove,
#                 caption=caption,
#                 is_first=is_first,
#                 is_last=is_last,
#                 can_reorder=can_reorder,
#                 return_path=return_path,
#                 )
#
#
# @register.inclusion_tag('bootstrap/_cms_inctag_news_pager.html')
# def cms_news_pager(page_prev, page_next):
#     return dict(
#                 page_prev=page_prev,
#                 page_next=page_next,
#                 )
