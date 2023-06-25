import os
from decouple import config



DEBUG = True

USE_TZ = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

USE_I18N = True

USE_L10N = True

DATABASES = {
	'default': {
		'HOST': config('DB_HOST'),
		'NAME': config('DB_NAME'),
		'PORT': config('DB_PORT'),
		'USER': config('DB_USER'),
		'ENGINE': "django.db.backends.postgresql_psycopg2",
		'PASSWORD': config('DB_PASSWORD'),
	}
}

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
			]
		}
	}
]

TIME_ZONE = 'UTC'

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'corsheaders.middleware.CorsMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SECRET_KEY = 's_b=5%2n=!(dehix7vlv*r3*si)+kjob3ev=6k%kknv%sd#hk2'

STATIC_URL = '/static/'

ROOT_URLCONF = 'blogreat.urls'

ALLOWED_HOSTS = ['*']

LANGUAGE_CODE = 'en-us'

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'corsheaders',
	'rest_framework',
	'blog',
	'cloudinary_storage',
	'cloudinary',
]

WSGI_APPLICATION = 'blogreat.wsgi.application'

CLOUDINARY_STORAGE = {
	'API_KEY': config('API_KEY'),
	'API_SECRET': config('API_SECRET'),
	'CLOUD_NAME': config('CLOUD_NAME'),
}

CORS_ALLOW_HEADERS = [
	'x-requested-with',
	'content-type',
	'accept',
	'origin',
	'authorization',
	'accept-encoding',
	'x-csrftoken',
	'access-control-allow-origin',
	'content-disposition',
]

CORS_ALLOW_METHODS = [
	'GET',
	'POST',
	'PUT',
	'PATCH',
	'DELETE',
	'OPTIONS',
]

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = False

AUTH_PASSWORD_VALIDATORS = [
	{'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
	{'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
	{'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
	{'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
