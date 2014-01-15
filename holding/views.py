from django.core.urlresolvers import reverse
from django.views.generic import TemplateView

from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)

from cms.models import Section
from cms.views import (
    ContentCreateView,
    ContentPageMixin,
    ContentPublishView,
    ContentRemoveView,
    ContentUpdateView,
)

from .forms import (
    HoldingContentEmptyForm,
    HoldingContentForm,
    TitleContentEmptyForm,
    TitleContentForm,
)
from .models import (
    HoldingContent,
    TitleContent,
)


class PageBaseView(ContentPageMixin, TemplateView):

    template_name = 'holding/page_content.html'

    def _get_body(self):
        return Section.objects.get(page=self.get_page(), layout__slug='body')

    def _get_home_page_footer(self):
        return Section.objects.get(page__slug='home', layout__slug='footer')


class PageDesignView(
        LoginRequiredMixin, StaffuserRequiredMixin, PageBaseView):

    def get_context_data(self, **kwargs):
        context = super(PageDesignView, self).get_context_data(**kwargs)
        section = self._get_body()
        contents = HoldingContent.objects.pending(section)
        if contents:
            c = contents[0]
        else:
            raise CmsError('Cannot find pending content for this section.')
        context.update(dict(
            design=True,
            content=c,
            footer_content=TitleContent.objects.pending(
                self._get_home_page_footer()
            ),
        ))
        return context


class PageView(PageBaseView):

    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        contents = HoldingContent.objects.published(self._get_body())
        if contents:
            c = contents[0]
        else:
            c = HoldingContent()
        context.update(dict(
            design=False,
            content=c,
            footer_content=TitleContent.objects.published(
                self._get_home_page_footer()
            ),
        ))
        return context


class HoldingContentPublishView(ContentPublishView):

    form_class = HoldingContentEmptyForm
    model = HoldingContent
    template_name = 'holding/content_publish.html'


class HoldingContentUpdateView(ContentUpdateView):

    form_class = HoldingContentForm
    model = HoldingContent
    template_name = 'holding/content_update.html'


class TitleContentPublishView(ContentPublishView):

    form_class = TitleContentEmptyForm
    model = TitleContent
    template_name = 'holding/title_publish.html'


class TitleContentUpdateView(ContentUpdateView):

    form_class = TitleContentForm
    model = TitleContent
    template_name = 'holding/title_update.html'
