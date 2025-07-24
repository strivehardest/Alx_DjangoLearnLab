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

# SECURITY SETTINGS

# ✅ Force all HTTP requests to redirect to HTTPS
SECURE_SSL_REDIRECT = True

# ✅ HTTP Strict Transport Security (HSTS) — force browsers to use HTTPS only
SECURE_HSTS_SECONDS = 31536000  # 1 year in seconds
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply to all subdomains
SECURE_HSTS_PRELOAD = True  # Allow domain to be preloaded into browsers' HSTS list

# ✅ Secure cookies — cookies only sent over HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# ✅ Security headers
X_FRAME_OPTIONS = 'DENY'  # Prevents clickjacking
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent content-type sniffing
SECURE_BROWSER_XSS_FILTER = True  # Enable browser XSS protection

# ✅ Set to False in production
DEBUG = False

# ✅ Replace with your actual production domain(s)
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Trust the X-Forwarded-Proto header from the proxy (e.g., NGINX) to identify secure requests
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
