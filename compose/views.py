# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)
from block.views import (
    ContentCreateView,
    ContentPublishView,
    ContentRemoveView,
    ContentUpdateView,
)

from .forms import (
    ArticleEmptyForm,
    ArticleForm,
)
from .models import (
    Article,
    ArticleBlock,
)


class ArticleCreateView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentCreateView):

    block_class = ArticleBlock
    form_class = ArticleForm
    model = Article
    template_name = 'compose/article_create.html'


class ArticlePublishView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentPublishView):

    form_class = ArticleEmptyForm
    model = Article
    template_name = 'compose/article_publish.html'


class ArticleRemoveView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentRemoveView):

    form_class = ArticleEmptyForm
    model = Article
    template_name = 'compose/article_remove.html'


class ArticleUpdateView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentUpdateView):

    form_class = ArticleForm
    model = Article
    template_name = 'compose/article_update.html'
