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
