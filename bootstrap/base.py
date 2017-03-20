# -*- encoding: utf-8 -*-
""" Django settings """
from django.core.urlresolvers import reverse_lazy

DEBUG = True
TESTING = False
THUMBNAIL_DEBUG = DEBUG

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

SITE_NAME = 'Compose'
COMPANY_NAME = 'KB Software'

ADMINS = (
    ('admin', 'code@pkimber.net'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = 'media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = 'web_static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'w@t8%tdwyi-n$u_s#4_+cwnq&6)1n)l3p-qe(ziala0j^vo12d'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'reversion.middleware.RevisionMiddleware',
)

ROOT_URLCONF = 'bootstrap.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'bootstrap.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
            'string_if_invalid': '**** INVALID EXPRESSION: %s ****',
        },
    },
]

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    #'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    # admin after login, so we prefer login templates
    'django.contrib.admin',
)

THIRD_PARTY_APPS = (
    'compressor',
    'easy_thumbnails',
    'reversion',
)



# `bootstrap` comes first so that it's version of `base`, `block`, and `compose`
# templates will be selected first.

LOCAL_APPS = (
    'bootstrap',
    'compose',
    'base',
    'block',
    'login',
    'mail',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# django-compressor
COMPRESS_ENABLED = False # defaults to the opposite of DEBUG

FTP_STATIC_DIR = None
FTP_STATIC_URL = None

# URL where requests are redirected after login when the contrib.auth.login
# view gets no next parameter.
LOGIN_REDIRECT_URL = reverse_lazy('project.dash')

# https://github.com/johnsensible/django-sendfile
SENDFILE_BACKEND = 'sendfile.backends.development'
SENDFILE_ROOT = 'media-private'


ARTICLE_WIDTH_HALFBIG = 'col-12 col-md-6'
ARTICLE_WIDTH_FULL = 'col-12'
ARTICLE_WIDTH_HALFORSMALLER = 'col-12 col-sm-6 col-md-4 col-lg-3 pure-xl-2'
ARTICLE_WIDTH_THIRDS = 'col-12 col-sm-6 col-md-4'

ARTICLE_TYPE_LEFT = 'pull-right'
ARTICLE_TYPE_RIGHT = 'pull-left'
ARTICLE_TYPE_TOP = 'w-100'
ARTICLE_TYPE_BOTTOM = 'w-100'
ARTICLE_TYPE_TEXT_ONLY = 'hidden'
ARTICLE_TYPE_PICTURE_ONLY = 'visible'

ARTICLE_IMAGE_SIZE_HALF = 'col-6'
ARTICLE_IMAGE_SIZE_THIRD = 'col-4'
ARTICLE_IMAGE_SIZE_QUARTER = 'col-3'

ARTICLE_WIDTH_CHOICES = (
    (ARTICLE_WIDTH_HALFBIG, 'Half when Big'),
    (ARTICLE_WIDTH_FULL, 'Full Width'),
    (ARTICLE_WIDTH_HALFORSMALLER, 'Half or Less'),
    (ARTICLE_WIDTH_THIRDS, 'Text Bottom'),
)

ARTICLE_TYPE_CHOICES = (
    (ARTICLE_TYPE_LEFT, 'Text Left'),
    (ARTICLE_TYPE_RIGHT, 'Text Right'),
    (ARTICLE_TYPE_TOP, 'Text Top'),
    (ARTICLE_TYPE_BOTTOM, 'Text Bottom'),
    (ARTICLE_TYPE_TEXT_ONLY, 'Text Only'),
    (ARTICLE_TYPE_PICTURE_ONLY, 'Picture Only'),
)

ARTICLE_IMAGE_SIZE_CHOICES = (
    (ARTICLE_IMAGE_SIZE_HALF, 'Half Width'),
    (ARTICLE_IMAGE_SIZE_THIRD, 'Third Width'),
    (ARTICLE_IMAGE_SIZE_QUARTER, 'Quarter Width'),
)
