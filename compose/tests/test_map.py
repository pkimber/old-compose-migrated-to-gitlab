# -*- encoding: utf-8 -*-
import pytest

from block.tests.helper import check_content
from compose.tests.factories import MapFactory


@pytest.mark.django_db
def test_content_methods():
    c = MapFactory()
    check_content(c)
