"""
Django settings for shop project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
# utf-8
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.utils import six

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jl68sas7+w)&$o(!r&s#f5e70g83#if=wtvpb7*=vn$5f+3t)t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# 调试工具
# DEBUG_TOOLBAR_PATCH_SETTINGS = False

ALLOWED_HOSTS = ['*']

# celery settings
import djcelery

djcelery.setup_loader()  # 目的是设定celery的加载器
CELERY_TIMEZONE = 'Asia/Shanghai'
# CELERY_BROKER_URL='amqp://zkyr:zkyr1006@111.207.68.150:5672/myvhost'#'redis://:zkyr1006@111.207.68.150:6379/10'
CELERY_BROKER_URL = 'redis://:zkyr1006@127.0.0.1:6379/10'
# CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'amqp://zkyr:zkyr1006@192.168.1.137:5672/myvhost'#'redis://:zkyr1006@111.207.68.150:6379/10'
# CELERY_RESULT_BACKEND = 'redis://localhost'#'django-db'  # 'django-cache'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'debug_toolbar.apps.DebugToolbarConfig',  # 调试工具App
    # 'users',#用户注册系统
    # 'djcelery',
    'django_celery_results',
    'df_user',
    'df_goods',
    'tinymce',
    'polls',
    'blog',
    # 'polls.apps.PollsConfig',  #完整安装路径
]
# AUTH_USER_MODEL = 'users.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',  # 调试工具中间件
]

ROOT_URLCONF = 'shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'shop.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shop',
        'USER': 'root',
        'PASSWORD': 'zkyr1006',
        'HOST': '111.207.68.150',
        'PORT': '3306',
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        # "LOCATION": "redis://:zkyr1006@127.0.0.1:6379/12",
        "LOCATION": "redis://127.0.0.1:6379/12",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # "SOCKET_CONNECT_TIMEOUT": 5,  # in seconds  套接字超时  socket 建立连接超时设置
            # "SOCKET_TIMEOUT": 5,  # in seconds  连接建立后的读写操作超时设置
            # "IGNORE_EXCEPTIONS": True,# redis 只作为缓存使用, 当它关闭时如果你不希望触发异常  忽略连接异常
            "PASSWORD": "zkyr1006"
        }
    }
}
REDIS_TIMEOUT = 7 * 24 * 60 * 60
CUBES_REDIS_TIMEOUT = 60 * 60
NEVER_REDIS_TIMEOUT = 365 * 24 * 60 * 60

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False  # 如果USE_TZ设置为True时，Django会使用系统默认设置的时区，即America/Chicago，
# 此时的TIME_ZONE不管有没有设置都不起作用。


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, '/home/zkfr/py/shop/static'),  #linux
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'static')
# MEDIA_ROOT = os.path.join(BASE_DIR,'/var/www/shop/static') #部署时建议部署到nginx等配置的静态文件目录

# #富文本编辑器配置
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    'width': 600,
    'height': 400,
}

#
# DEBUG_TOOLBAR_PANELS = [
#     'debug_toolbar.panels.versions.VersionsPanel',
#     'debug_toolbar.panels.timer.TimerPanel',
#     'debug_toolbar.panels.settings.SettingsPanel',
#     'debug_toolbar.panels.headers.HeadersPanel',
#     'debug_toolbar.panels.request.RequestPanel',
#     'debug_toolbar.panels.sql.SQLPanel',
#     'debug_toolbar.panels.staticfiles.StaticFilesPanel',
#     'debug_toolbar.panels.templates.TemplatesPanel',
#     'debug_toolbar.panels.cache.CachePanel',
#     'debug_toolbar.panels.signals.SignalsPanel',
#     'debug_toolbar.panels.logging.LoggingPanel',
#     'debug_toolbar.panels.redirects.RedirectsPanel',
# ]
# CONFIG_DEFAULTS = {
#     # Toolbar options
#     'DISABLE_PANELS': {'debug_toolbar.panels.redirects.RedirectsPanel'},
#     'INSERT_BEFORE': '</body>',
#     'JQUERY_URL': '//cdn.bootcss.com/jquery/2.1.4/jquery.min.js',
#     'RENDER_PANELS': None,
#     'RESULTS_CACHE_SIZE': 10,
#     'ROOT_TAG_EXTRA_ATTRS': '',
#     'SHOW_COLLAPSED': False,
#     'SHOW_TOOLBAR_CALLBACK': 'debug_toolbar.middleware.show_toolbar',
#     # Panel options
#     'EXTRA_SIGNALS': [],
#     'ENABLE_STACKTRACES': True,
#     'HIDE_IN_STACKTRACES': (
#         'socketserver' if six.PY3 else 'SocketServer',
#         'threading',
#         'wsgiref',
#         'debug_toolbar',
#         'django',
#     ),
#     'PROFILER_MAX_DEPTH': 10,
#     'SHOW_TEMPLATE_CONTEXT': True,
#     'SKIP_TEMPLATE_PREFIXES': (
#         'django/forms/widgets/',
#         'admin/widgets/',
#     ),
#     'SQL_WARNING_THRESHOLD': 500,   # milliseconds
# }
# INTERNAL_IPS = ("127.0.0.1",)  # 调试工具的IP


# 打印sql功能
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'INFO',
        },
    },
}
# #用户注册系统
# USERS_REGISTRATION_OPEN = False
#
# USERS_VERIFY_EMAIL = True
#
# USERS_AUTO_LOGIN_ON_ACTIVATION = True
#
# USERS_EMAIL_CONFIRMATION_TIMEOUT_DAYS = 3
#
# # Specifies minimum length for passwords:
# USERS_PASSWORD_MIN_LENGTH = 5
#
# # Specifies maximum length for passwords:
# USERS_PASSWORD_MAX_LENGTH = None
#
# # the complexity validator, checks the password strength
# USERS_CHECK_PASSWORD_COMPLEXITY = True
#
# USERS_SPAM_PROTECTION = False  # important!

#  ---------------------------------------------------------
#  Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.163.com'  # 如果是 163 改成 smtp.163.com
EMAIL_PORT = 25  # smtp服务固定的端口是25
EMAIL_HOST_USER = 'chengnian_20@163.com'  # 发送邮件的邮箱
EMAIL_HOST_PASSWORD = 'zkyr1006'  # #在邮箱中设置的客户端授权密码
EMAIL_FROM = 'cheng<chengnian_20@163.com>'
