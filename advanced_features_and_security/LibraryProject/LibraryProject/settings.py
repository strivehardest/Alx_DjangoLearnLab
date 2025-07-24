# settings.py

SECRET_KEY = 'your-secret-key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']



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

# ✅ Secure cookies over HTTPS only
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# ✅ Browser-level XSS protection
SECURE_BROWSER_XSS_FILTER = True

# ✅ Prevent content sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True

# ✅ Prevent clickjacking
X_FRAME_OPTIONS = 'DENY'

# ✅ Optional CSP header setup (also covered in Step 4)
CSP_DEFAULT_SRC = ("'self'",)

# ✅ Allowed hosts for deployment
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']  # Replace with actual domains

# ✅ Only allow HTTPS (optional)
SECURE_SSL_REDIRECT = True  # Only if you have HTTPS setup

MIDDLEWARE = [
    # ...
    'csp.middleware.CSPMiddleware',
]

CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'", 'https://trusted-cdn.com')
CSP_STYLE_SRC = ("'self'", 'https://trusted-cdn.com')
