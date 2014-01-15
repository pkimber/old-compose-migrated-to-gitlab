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
    TitleContentEmptyForm,
    TitleContentForm,
)
from .models import TitleContent


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
        context.update(dict(
            design=True,
            footer_content=TitleContent.objects.pending(
                self._get_home_page_footer()
            ),
            #stripe_content=HoldingContent.objects.pending(section),
            #stripe_create_url=reverse(
            #    'project.stripe.create',
            #    kwargs=dict(
            #        page=section.page.slug,
            #        layout=section.layout.slug,
            #    )
            #),
        ))
        return context


class PageView(PageBaseView):

    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        context.update(dict(
            design=False,
            footer_content=TitleContent.objects.published(
                self._get_home_page_footer()
            ),
            #stripe_content=StripeContent.objects.published(self._get_body()),
        ))
        return context


class TitleContentPublishView(ContentPublishView):

    form_class = TitleContentEmptyForm
    model = TitleContent
    template_name = 'holding/title_publish.html'


class TitleContentUpdateView(ContentUpdateView):

    form_class = TitleContentForm
    model = TitleContent
    template_name = 'holding/title_update.html'
