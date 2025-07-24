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
