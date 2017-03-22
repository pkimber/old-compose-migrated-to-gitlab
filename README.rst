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

  virtualenv --python=python3 venv-compose
  source venv-compose/bin/activate

  pip install -r requirements/local.txt

Testing
=======

::

  find . -name '*.pyc' -delete
  py.test -x

.. important:: Don't forget to use the ``--create-db`` parameter on ``pytest``
               the first time.

Usage
=====

::

  ./init_dev.sh

Release and Deploy
==================

https://www.kbsoftware.co.uk/docs/
