INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',  # your app with the CustomUser model
]

AUTH_USER_MODEL = 'bookshelf.CustomUser'

DEBUG = False  # ✅ Never True in production

