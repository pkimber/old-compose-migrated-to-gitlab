# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)

from block.views import (
    ContentPublishView,
    ContentUpdateView,
)

from .forms import (
    HoldingEmptyForm,
    HoldingForm,
    TitleEmptyForm,
    TitleForm,
)
from .models import (
    Holding,
    Title,
)


#class PageBaseView(ContentPageMixin, TemplateView):
#
#    template_name = 'holding/page_content.html'
#
#    def _get_body(self):
#        return Section.objects.get(slug=SECTION_BODY)
#
#    def _get_footer(self):
#        return Section.objects.get(slug=SECTION_FOOTER)
#
#    def _get_home_page(self):
#        return Page.objects.get(slug=PAGE_HOME)
#
#
#class PageDesignView(
#        LoginRequiredMixin, StaffuserRequiredMixin, PageBaseView):
#
#    def get_context_data(self, **kwargs):
#        context = super(PageDesignView, self).get_context_data(**kwargs)
#        page = self.get_page()
#        body = self._get_body()
#        contents = Holding.objects.pending(page, body)
#        if contents:
#            c = contents[0]
#        else:
#            raise BlockError('Cannot find pending content for this section.')
#        context.update(dict(
#            design=True,
#            content=c,
#            footer_content=Title.objects.pending(
#                self._get_home_page(),
#                self._get_footer(),
#            ),
#        ))
#        return context
#
#
#class PageView(PageBaseView):
#
#    def get_context_data(self, **kwargs):
#        context = super(PageView, self).get_context_data(**kwargs)
#        contents = Holding.objects.published(
#            self.get_page(),
#            self._get_body(),
#        )
#        if contents:
#            c = contents[0]
#        else:
#            c = Holding()
#        context.update(dict(
#            design=False,
#            content=c,
#            footer_content=Title.objects.published(
#                self._get_home_page(),
#                self._get_footer(),
#            ),
#        ))
#        return context


class HoldingPublishView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentPublishView):

    form_class = HoldingEmptyForm
    model = Holding
    template_name = 'compose/holding_publish.html'


class HoldingUpdateView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentUpdateView):

    form_class = HoldingForm
    model = Holding
    template_name = 'compose/holding_update.html'


class TitlePublishView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentPublishView):

    form_class = TitleEmptyForm
    model = Title
    template_name = 'compose/title_publish.html'


class TitleUpdateView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentUpdateView):

    form_class = TitleForm
    model = Title
    template_name = 'compose/title_update.html'
