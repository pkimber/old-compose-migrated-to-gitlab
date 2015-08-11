# -*- encoding: utf-8 -*-
import pytest

from block.tests.helper import check_content
from compose.tests.factories import SlideshowFactory


@pytest.mark.django_db
def test_content_methods():
    c = SlideshowFactory()
    check_content(c)
