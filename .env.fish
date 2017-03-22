source venv-compose/bin/activate.fish
set -x DJANGO_SETTINGS_MODULE "example_compose.dev_patrick"
set -x MAIL_TEMPLATE_TYPE "django"
set -x NORECAPTCHA_SECRET_KEY "your secret key"
set -x NORECAPTCHA_SITE_KEY "your site key"
set -x OPBEAT_APP_ID "app-id"
set -x OPBEAT_ORGANIZATION_ID "organization-id"
set -x OPBEAT_SECRET_TOKEN "secret-token"
set -x SECRET_KEY "the_secret_key"
source .private
