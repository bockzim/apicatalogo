from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

secret_key_valor = 'chave-de-desenvolvimento'
SECRET_KEY = secret_key_valor
DEBUG = True
ALLOWED_HOSTS = ['*']

# apps
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_spectacular',
    'catalogo',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    dict(
        BACKEND='django.template.backends.django.DjangoTemplates',
        DIRS=[],
        APP_DIRS=True,
        OPTIONS=dict(context_processors=[]),
    ),
]

# banco
DATABASES = dict(
    default=dict(
        ENGINE='django.db.backends.sqlite3',
        NAME=BASE_DIR / 'db.sqlite3',
    )
)

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# drf, jwt e swagger
REST_FRAMEWORK = dict(
    DEFAULT_AUTHENTICATION_CLASSES=[
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    DEFAULT_PERMISSION_CLASSES=[
        'rest_framework.permissions.IsAuthenticated',
    ],
    DEFAULT_SCHEMA_CLASS='drf_spectacular.openapi.AutoSchema',
)

SPECTACULAR_SETTINGS = dict(
    TITLE='catalogo de filmes',
    VERSION='1.0.0',
)
