Holding
*******

Django application for a simple CMS site

Install
=======

Virtual Environment
-------------------

::

  pyvenv-3.4 --without-pip venv-cms
  source venv-cms/bin/activate
  wget https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py
  python get-pip.py

  pip install -r requirements/local.txt

Testing
=======

::

  find . -name '*.pyc' -delete
  py.test -x

Usage
=====

::

  ./init_dev.sh

Release
=======

https://www.pkimber.net/open/


Compose Blocks
==============

Article
-------

See the template in compose/page_article.html.  This is used by the home page of the example app.


Feature
-------

Provides a page section with a title, description and a picture

See the template compose/page_feature.html (this uses the compose/_event_feature.html
snippet which displays events using the feature block). This page is not created when 
the example_cms app is initialised so you need to log in to the exmaple_cms app
as 'admin' and follow this procedure to configure it.  Please note this page also
uses a header block so you need to configure it (see the section below).

Create a section with a slug of 'feature_a' (Dashboard | Section)

Create a template called 'compose/page_feature.html'  (Dashboard | Template).
Add the Feature A section created above.

Create a Feature style called 'Event' css class 'event' (Settings | Feature Styles)

Create a page that uses the page_feature template (dashboard | Create Page)

You can now manage the content on this page using design mode.

Header
------

Provides a page section that displays a header.

See the template page_feature.html. In addition to the steps above

Create a section with a slug of 'header_a' (Dashboard | Section) Add this
section to the template compose/page_feature.html created above (dashboard | Template)

You can now manage the content on this page using design mode 
