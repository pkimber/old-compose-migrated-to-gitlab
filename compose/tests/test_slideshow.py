# -*- encoding: utf-8 -*-
import pytest

from block.tests.helper import check_content
from block.tests.factories import ImageFactory
from compose.tests.factories import (
    SlideshowBlockFactory,
    SlideshowFactory,
)
from login.tests.factories import UserFactory


@pytest.mark.django_db
def test_content_methods():
    c = SlideshowFactory()
    check_content(c)


@pytest.mark.django_db
def test_publish():
    block = SlideshowBlockFactory()
    c = SlideshowFactory(
        block=block,
        slideshow=(ImageFactory(), ImageFactory()),
    )
    block.publish(UserFactory())
    assert 2 == block.get_pending().slideshow.count()
    assert 2 == block.get_published().slideshow.count()
