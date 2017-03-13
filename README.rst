Compose
*******

Django application containing a couple of models for use with the block app
when building a simple CMS site.

.. important:: We will put the panel system into this app.

Install
=======

Virtual Environment
-------------------

::

  virtualenv --python=python3.5 venv-compose
  source venv-compose/bin/activate
  pip install --upgrade pip

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
