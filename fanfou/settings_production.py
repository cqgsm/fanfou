
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 's_e=+hv5db*3(2jc59o4hxta5&a^#9j^gan8l!xxi58c4(o-5a'

DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'fanfou.apps.wechat','fanfou.apps.user','fanfou.apps.dating','fanfou.apps.qiniu',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework','rest_framework.authtoken','corsheaders','rest_framework_docs',
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 15
}

REST_FRAMEWORK_DOCS = {
    'HIDE_DOCS': os.environ.get('HIDE_DRFDOCS', False)
}

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'fanfou.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'fanfou.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/home/ymgit/fanfou/fanfou/caches',
        # 'TIMEOUT': 600,
        # 'OPTIONS': {
        #     'MAX_ENTRIES': 1000
        # }
    }
}


WECHAT = {
    'APPID':'wx2fc60b4541356e82',
    'APPSECRET':'1b5ddf26c657f363a9afd25760266f27',
    'TOKEN':'linqiaohui1995',
}

LANGUAGE_CODE = 'zh-CN'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,"static")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
