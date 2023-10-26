"""
Django sozlamalari loyihasi.

Django 4.2.6-da yaratilgan.
Batafsil ma'lumotlar uchun quyidagi manzilni ko'ring:
https://docs.djangoproject.com/en/4.2/topics/settings/

Sozlamalar va ularning qiymatlari ro'yxati uchun quyidagi manzilni ko'ring:
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Loyiha ichidagi yo'l tugmachalari: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Tezkor boshlash uchun sozlamalar - ishlab chiqish uchun mos kelmaydi
# Ko'proq ma'lumot uchun quyidagi manzilni ko'ring: https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# XAVFSIZLIK EHTIYOTKARLIK: ishlab chiqarishda ishlatiladigan maxfiy kaliti himoyalang!
SECRET_KEY = 'django-insecure-5_m22m^m8u4m5zm=9%g0x4-=wp()+$8#sge6c43*m6c#s=(f_('

# XAVFSIZLIK EHTIYOTKARLIK: ishlab chiqarishda debug yoqilgan holatda ishlatilmaydi!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']

# Loyiha tuzilmasi
INSTALLED_APPS = [
    'jazzmin',
    'account',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news',
    'hitcount',
    'modeltranslation',
    'whitenoise',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'setting.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'news.context.contexts',
            ],
        },
    },
]

WSGI_APPLICATION = 'setting.wsgi.application'

# Ma'lumotlar bazasi
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Parolni tekshirish
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

# Xalqaro holatlar
LANGUAGE_CODE = 'uz'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True

from django.utils.translation import gettext_lazy as _
LANGUAGES = [
    ('uz', _("Uzbek")),
    ('en', _("English")),
    ('ru', _("Russian")),
]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'
import os
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

# STATIK URL: CSS, JavaScript, Rasm
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = 'meida/'
MEDIA_ROOT = BASE_DIR / 'media'

# STANDART SOHA XATASI
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
