# -*- encoding: utf-8 -*-
""" Django settings """
from django.core.urlresolvers import reverse_lazy

DEBUG = True
TESTING = False
THUMBNAIL_DEBUG = DEBUG

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

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

ROOT_URLCONF = 'example_compose.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'example_compose.wsgi.application'

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
                'django.template.context_processors.request',
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
    'easy_thumbnails',
    'reversion',
    'taggit',
)

LOCAL_APPS = (
    'base',
    'block',
    'compose',
    'example_compose',
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

FTP_STATIC_DIR = None
FTP_STATIC_URL = None

# URL where requests are redirected after login when the contrib.auth.login
# view gets no next parameter.
LOGIN_REDIRECT_URL = reverse_lazy('project.dash')

# https://github.com/johnsensible/django-sendfile
SENDFILE_BACKEND = 'sendfile.backends.development'
SENDFILE_ROOT = 'media-private'


CSS_WIDTH_HALFBIG = 'pure-u-1 pure-md-1-2'
CSS_WIDTH_FULL = 'pure-u-1'
CSS_WIDTH_HALFORSMALLER = 'pure-sm-1-2 pure-lg-1-3 pure-xl-1-4'
CSS_WIDTH_THIRDS = 'pure-u-1-3'

CSS_WIDTHS = (
    (CSS_WIDTH_HALFBIG, 'Half when Big'),
    (CSS_WIDTH_FULL, 'Full Width'),
    (CSS_WIDTH_HALFORSMALLER, 'Half or Less'),
    (CSS_WIDTH_THIRDS, 'Text Bottom'),
)


CSS_TEXT_LEFT = 'text_left'
CSS_TEXT_RIGHT = 'text_right'
CSS_TEXT_TOP = 'text_top'
CSS_TEXT_BOTTOM = 'text_bottom'
CSS_TEXT_ONLY = 'text_only'
CSS_PICTURE_ONLY = 'picture_only'

CSS_TEXT_POSITION = (
    (CSS_TEXT_LEFT, 'Text Left'),
    (CSS_TEXT_RIGHT, 'Text Right'),
    (CSS_TEXT_TOP, 'Text Top'),
    (CSS_TEXT_BOTTOM, 'Text Bottom'),
    (CSS_TEXT_ONLY, 'Text Only'),
    (CSS_PICTURE_ONLY, 'Picture Only'),
)


CSS_IMAGE_SIZE_HALF = '1-2'
CSS_IMAGE_SIZE_THIRD = '1-3'
CSS_IMAGE_SIZE_QUARTER = '1-4'

CSS_IMAGE_SIZES = (
    (CSS_IMAGE_SIZE_HALF, 'Half Width'),
    (CSS_IMAGE_SIZE_THIRD, 'Third Width'),
    (CSS_IMAGE_SIZE_QUARTER, 'Quarter Width'),
)
