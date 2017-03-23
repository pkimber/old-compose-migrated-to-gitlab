#!/bin/bash
# exit immediately if a command exits with a nonzero exit status.
set -e
# treat unset variables as an error when substituting.
set -u

py.test -x -s
touch temp.db && rm temp.db
django-admin.py migrate --noinput
django-admin.py demo_data_login
django-admin.py init_app_block
django-admin.py bootstrap_demo
# for the 'css' code snippet
django-admin.py demo_data_compose

django-admin.py runserver 0.0.0.0:8000
