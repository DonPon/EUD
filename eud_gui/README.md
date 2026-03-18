# Project Configuration (`eud_gui/`)

## Purpose
The `eud_gui` directory is the configuration core of the Django project. It contains the primary settings, root URL routing, and server entry points (WSGI/ASGI).

## Relevant Files

### 1. `settings.py`
This is the most critical file in the project. It defines:
- **`INSTALLED_APPS`**: Lists all local apps (`apps.*`) and third-party libraries (`rest_framework`, `simple_history`).
- **`MIDDLEWARE`**: Includes custom middleware like `DevSSOMiddleware` for authentication simulation.
- **`AUTH_USER_MODEL`**: Configured to use the custom user model (`apps.users.User`).
- **`REST_FRAMEWORK`**: Global configuration for API pagination, permissions, and authentication.
- **Database & Static Files**: Connection strings and paths for static/media assets.

### 2. `urls.py`
The root URL dispatcher. It maps high-level paths to their respective applications:
- `/api/`: Routes to the `generic_crud` engine.
- `/api/audit/`: Routes to the history/audit system.
- `/users/`: User management and login/logout.
- `/dashboard/`: RPA bot execution monitoring.
- Root (`/`): Shared views from `apps.core` and `apps.clients`.

### 3. `wsgi.py` & `asgi.py`
Entry point files for deployment. `wsgi.py` is used for traditional synchronous web servers (e.g., Gunicorn), while `asgi.py` supports asynchronous protocols.

## Impact of Changes

| Change | Impact |
| :--- | :--- |
| **Modifying `settings.py`** | Global impact. Can change database connections, security policies, or enable/disable entire features (like DRF settings). |
| **Adding a route to `urls.py`** | Exposes new URLs at the top level of the application. |
| **Changing `MIDDLEWARE`** | Affects the request/response lifecycle for every single request (e.g., how users are authenticated). |

## Guidelines
- Avoid placing application-specific logic here. Keep this directory strictly for project-wide orchestration.
- Sensitive values (like `SECRET_KEY`) should ideally be moved to environment variables for production environments.
