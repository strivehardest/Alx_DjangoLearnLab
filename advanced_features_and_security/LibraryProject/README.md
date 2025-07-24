### Permissions and Groups Setup (Developer Notes)

#### Custom Permissions in `Book` Model:
- `can_view`: View books
- `can_create`: Create new books
- `can_edit`: Edit existing books
- `can_delete`: Delete books

#### Groups:
- **Viewers** → Only `can_view`
- **Editors** → `can_view`, `can_create`, `can_edit`
- **Admins** → All permissions

#### Usage in Views:
Permissions are enforced using `@permission_required` decorators in `bookshelf/views.py`.
Use `raise_exception=True` to return `403 Forbidden` if unauthorized.

Test by logging in as users from different groups and accessing the respective views.

# Django Security Hardening – Summary

## Configurations in `settings.py`:
- `DEBUG = False`
- `CSRF_COOKIE_SECURE`, `SESSION_COOKIE_SECURE = True`
- `SECURE_BROWSER_XSS_FILTER`, `SECURE_CONTENT_TYPE_NOSNIFF = True`
- `X_FRAME_OPTIONS = 'DENY'`
- `SECURE_SSL_REDIRECT = True`
- `CSP_*` headers via `django-csp`

## Views:
- All user input is validated using Django forms.
- ORM is used for all database queries (no raw SQL).

## Templates:
- `{% csrf_token %}` included in all POST forms.

## Tested By:
- Manually submitting unsafe scripts
- Submitting forms without CSRF
- Invalid input injection testing

# 🔐 HTTPS & Security Hardening Overview

## Django Security Settings Configured

| Setting | Description |
|--------|-------------|
| `SECURE_SSL_REDIRECT = True` | Redirects all HTTP traffic to HTTPS |
| `SECURE_HSTS_SECONDS = 31536000` | Enforces HTTPS in browsers for 1 year |
| `SECURE_HSTS_INCLUDE_SUBDOMAINS = True` | Applies HSTS to subdomains |
| `SECURE_HSTS_PRELOAD = True` | Preload domain in browser HSTS lists |
| `SESSION_COOKIE_SECURE = True` | Session cookies only over HTTPS |
| `CSRF_COOKIE_SECURE = True` | CSRF cookies only over HTTPS |
| `X_FRAME_OPTIONS = 'DENY'` | Blocks clickjacking via iframes |
| `SECURE_CONTENT_TYPE_NOSNIFF = True` | Prevents MIME-type sniffing |
| `SECURE_BROWSER_XSS_FILTER = True` | Enables browser’s XSS filter |

## Deployment
- Configured NGINX to redirect HTTP to HTTPS.
- SSL/TLS enabled using a valid certificate.

## Testing
- Verified automatic redirects from HTTP to HTTPS.
- Used browser dev tools and SSL Labs to confirm secure headers and encryption.
