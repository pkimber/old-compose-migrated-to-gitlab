# -*- encoding: utf-8 -*-
import pytest

from block.tests.helper import check_content
from block.tests.factories import ImageFactory
from compose.tests.factories import (
    SidebarBlockFactory,
    SidebarFactory,
)
from login.tests.factories import UserFactory


@pytest.mark.django_db
def test_content_methods():
    c = SidebarFactory()
    check_content(c)


@pytest.mark.django_db
def test_publish():
    block = SidebarBlockFactory()
    c = SidebarFactory(block=block, title="TITLE")
    block.publish(UserFactory())
    assert "TITLE" == block.get_pending().title
    assert "TITLE" == block.get_published().title
