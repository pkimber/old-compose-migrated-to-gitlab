# -*- encoding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.views.generic.edit import (
    CreateView,
    UpdateView,
)
from django.views.generic.list import ListView

from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)

from base.view_utils import BaseMixin
from block.forms import ContentEmptyForm
from block.views import (
    ContentCreateView,
    ContentPublishView,
    ContentRemoveView,
    ContentUpdateView,
)

from .forms import (
    ArticleForm,
    CodeSnippetCreateForm,
    CodeSnippetUpdateForm,
    FeatureForm,
    FeatureStyleForm,
    HeaderForm,
    HeaderStyleForm,
    MapForm,
    SidebarForm,
    SlideshowForm,
)
from .models import (
    Article,
    ArticleBlock,
    CodeSnippet,
    Feature,
    FeatureBlock,
    FeatureStyle,
    Header,
    HeaderBlock,
    HeaderStyle,
    Map,
    MapBlock,
    Sidebar,
    SidebarBlock,
    Slideshow,
    SlideshowBlock,
)


class ArticleCreateView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentCreateView):

    block_class = ArticleBlock
    form_class = ArticleForm
    model = Article
    template_name = 'compose/article_create.html'


class ArticlePublishView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentPublishView):

    form_class = ContentEmptyForm
    model = Article
    template_name = 'compose/article_publish.html'


class ArticleRemoveView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentRemoveView):

    form_class = ContentEmptyForm
    model = Article
    template_name = 'compose/article_remove.html'


class ArticleUpdateView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentUpdateView):

    form_class = ArticleForm
    model = Article
    template_name = 'compose/article_update.html'


class CodeSnippetCreateView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, CreateView):

    form_class = CodeSnippetCreateForm
    model = CodeSnippet

    def get_success_url(self):
        return reverse('compose.code.snippet.list')


class CodeSnippetListView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, ListView):

    model = CodeSnippet
    paginate_by = 15


class CodeSnippetUpdateView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, UpdateView):

    form_class = CodeSnippetUpdateForm
    model = CodeSnippet

    def get_success_url(self):
        return reverse('compose.code.snippet.list')


class FeatureCreateView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentCreateView):

    block_class = FeatureBlock
    form_class = FeatureForm
    model = Feature
    template_name = 'compose/feature_create_update.html'


class FeaturePublishView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentPublishView):

    form_class = ContentEmptyForm
    model = Feature
    template_name = 'compose/feature_publish.html'


class FeatureRemoveView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentRemoveView):

    form_class = ContentEmptyForm
    model = Feature
    template_name = 'compose/feature_remove.html'


class FeatureUpdateView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentUpdateView):

    form_class = FeatureForm
    model = Feature
    template_name = 'compose/feature_create_update.html'


class FeatureStyleCreateView(
        LoginRequiredMixin, StaffuserRequiredMixin, CreateView):
    form_class = FeatureStyleForm
    model = FeatureStyle
    template_name = 'compose/style_create_update.html'

    def get_success_url(self):
        return reverse('compose.feature.style.list')


class FeatureStyleUpdateView(
        LoginRequiredMixin, StaffuserRequiredMixin, UpdateView):
    form_class = FeatureStyleForm
    model = FeatureStyle
    template_name = 'compose/style_create_update.html'

    def get_success_url(self):
        return reverse('compose.feature.style.list')


class HeaderCreateView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentCreateView):

    block_class = HeaderBlock
    form_class = HeaderForm
    model = Header
    template_name = 'compose/header_create_update.html'


class HeaderPublishView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentPublishView):

    form_class = ContentEmptyForm
    model = Header
    template_name = 'compose/header_publish.html'


class HeaderUpdateView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentUpdateView):

    form_class = HeaderForm
    model = Header
    template_name = 'compose/header_create_update.html'


class HeaderRemoveView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentRemoveView):

    form_class = ContentEmptyForm
    model = Header
    template_name = 'compose/header_remove.html'


class HeaderStyleCreateView(
        LoginRequiredMixin, StaffuserRequiredMixin, CreateView):
    form_class = HeaderStyleForm
    model = HeaderStyle
    template_name = 'compose/style_create_update.html'

    def get_success_url(self):
        return reverse('compose.header.style.list')


class HeaderStyleUpdateView(
        LoginRequiredMixin, StaffuserRequiredMixin, UpdateView):
    form_class = HeaderStyleForm
    model = HeaderStyle
    template_name = 'compose/style_create_update.html'

    def get_success_url(self):
        return reverse('compose.header.style.list')


class FeatureStyleListView(
        LoginRequiredMixin, StaffuserRequiredMixin, ListView):
    model = FeatureStyle


class HeaderStyleListView(
        LoginRequiredMixin, StaffuserRequiredMixin, ListView):
    model = HeaderStyle


class MapCreateView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentCreateView):

    block_class = MapBlock
    form_class = MapForm
    model = Map
    template_name = 'compose/map_form.html'


class MapPublishView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentPublishView):

    form_class = ContentEmptyForm
    model = Map
    template_name = 'compose/map_publish.html'


class MapRemoveView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentRemoveView):

    form_class = ContentEmptyForm
    model = Map
    template_name = 'compose/map_remove.html'


class SidebarCreateView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentCreateView):

    block_class = SidebarBlock
    form_class = SidebarForm
    model = Sidebar
    template_name = 'compose/sidebar_form.html'


class SidebarPublishView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentPublishView):

    form_class = ContentEmptyForm
    model = Sidebar
    template_name = 'compose/sidebar_publish.html'


class SidebarRemoveView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentRemoveView):

    form_class = ContentEmptyForm
    model = Sidebar
    template_name = 'compose/sidebar_remove.html'


class SidebarUpdateView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentUpdateView):

    form_class = SidebarForm
    model = Sidebar
    template_name = 'compose/sidebar_form.html'


class SlideshowCreateView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentCreateView):

    block_class = SlideshowBlock
    form_class = SlideshowForm
    model = Slideshow
    template_name = 'compose/slideshow_create.html'


class SlideshowPublishView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentPublishView):

    form_class = ContentEmptyForm
    model = Slideshow
    template_name = 'compose/slideshow_publish.html'


class SlideshowRemoveView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentRemoveView):

    form_class = ContentEmptyForm
    model = Slideshow
    template_name = 'compose/slideshow_remove.html'


class SlideshowUpdateView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentUpdateView):

    form_class = SlideshowForm
    model = Slideshow
    template_name = 'compose/slideshow_update.html'
