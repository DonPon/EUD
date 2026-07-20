# Europe Domestic GUI (EUD) - Project Instructions

## Project Overview
The **Europe Domestic GUI (EUD)** is a Django-based application designed to control bot execution and manage client data. It features a robust **Generic CRUD Engine** that allows for rapid development of data management interfaces.

### Core Technologies
- **Backend:** Django 6.x, Django REST Framework (DRF)
- **Database:** PostgreSQL (Production) / SQLite (Local Development)
- **Auditing:** `django-simple-history`
- **Configuration:** YAML-based config with custom loader
- **Frontend:** Server-side rendered templates with dynamic DataTables and custom generic forms.

### Architecture
- **Star Schema:** All client-related data is linked through a `client_uuid`. The `BankingRelationship` model serves as the central hub.
- **ClientRelatedModel:** Base class for all client-related models (`apps/core/models.py`). It provides `client_uuid`, `created_at`, `updated_at`, and automatic audit logging via `django-simple-history`.
- **User Roles:** Custom user model (`apps/users/models.py`) uses T-Numbers as usernames and supports three roles:
    - `ADMIN`: Full access to all features and user management.
    - `EDITOR`: Can create and edit client data, but cannot manage users.
    - `VIEWER`: Read-only access to client data.
- **Generic CRUD Engine:** Located in `apps/generic_crud/`, this engine dynamically generates API endpoints, serializers, and HTML forms for any registered model.
- **Modular Apps:**
    - `apps/clients`: Natural Person (NP) client models and registration.
    - `apps/clients_le`: Legal Entity (LE) client models and registration.
    - `apps/generic_crud`: The core logic for dynamic UI/API generation.
    - `apps/users`: Custom user management with role-based permissions.
    - `apps/audit`: History and audit logging views.
    - `apps/dashboard_bots`: Bot execution control and visualization.
    - `apps/repapering`: Document requirement scenario mappings (onboarding).

---

## Building and Running

### Prerequisites
uv venv located in .venv, to be activated using:
```bash
source /Users/franz/Code/EUD/.venv/bin/activate
```

- Python 3.10+
- Dependencies listed in `requirements.txt`

### Key Commands

#### Development Server
The application uses a custom launcher to handle configuration files.
```bash
# Recommended: Run with auto-open browser
python start_app.py --port 8003

# Run with custom configuration (PostgreSQL)
python start_app.py --config-file "path/to/config.yaml" --port 8003
```

#### Seeding Data
Seed scripts are located in the `seeds/` directory and should be run after migration.
```bash
# Full setup (User + Clients + Bots)
python seeds/full_setup.py

# Individual seed scripts
python seeds/create_user.py
python seeds/bulk_seed.py --count 20
python seeds/seed_bots.py
```

#### Running Tests
Do not run tests; user will do it manually.
```bash
python manage.py test
```

---

## Development Conventions

### Adding New Models
1.  **Define Model:** Inherit from `ClientRelatedModel` in `apps/clients/models.py` (NP) or `apps/clients_le/models.py` (LE).
2.  **Register Model:** Add the model to `apps/clients/registration.py` or `apps/clients_le/registration.py`.
    - Provide `fields` for forms/API.
    - Provide `list_display` for the table view.
3.  **Migrate:** Run `makemigrations` and `migrate`.

### Git & Committing
- **No automatic commits or pushes:** Never commit or push changes unless explicitly instructed by the user.

### Coding Standards
- **Surgical Changes:** Only modify the registry and models to add/remove fields.
- **Client Linking:** Always ensure `client_uuid` is handled correctly. For new related models, the CRUD engine handles `client_uuid` injection from GET parameters automatically.
- **Permissions:** Default permissions are role-based. Use `RoleBasedPermission` or specify `permission_classes` in the registry config.
- **UI Customization:**
    - Use `list_display` in the registry for table columns.
    - Use `_apply_dynamic_choices` in `apps/generic_crud/views.py` for fields requiring dynamic dropdowns (e.g., linked products).

---

## Re-papering Module (`apps/repapering/`)

The Repapering module defines **document requirement scenarios** — mappings between banking scenarios (e.g., "A - Natural Person Resident") and the documents needed for each. It serves as the single source of truth consumed by the core banking logic.

### Data Models
- **Scenario** (`UUID PK`, `name`): A banking scenario category. Has many `DocumentRequirement` records.
- **DocumentRequirement** (`UUID PK`, FK to `Scenario`, `cdok`, `duplicate`, `granularity`, `output_folder_structure`, `pdf_template`): Maps a document code to a scenario with granularity rules and optional PDF template.

### UI Workflow
1. **Scenario List** (`/repapering/`) — lists all scenarios with a "View / Map Docs" button.
2. **Scenario Detail** (`/repapering/scenario/<id>/`) — shows mapped documents; "Add Document Mapping", edit, delete (also removes PDF template).
3. **Create/Edit forms** — rendered by the Generic CRUD engine; `scenario` FK is pre-selected via GET parameter.

### Permissions
- **ADMIN:** Full CRUD + Export/Import JSON.
- **EDITOR:** View scenarios, add/edit/delete document mappings (no export/import).
- **VIEWER:** Read-only access.

### Import / Export
- Export: Downloads all scenarios + document requirements as JSON (`repapering_settings.json`).
- Import: Atomic upsert — scenarios matched by name, requirements fully replaced.
- **ADMIN only.**

### Custom Views (not Generic CRUD)
- `ScenarioListView`, `ScenarioDetailView`, `DocumentRequirementDeleteView`, `ExportRepaperingView`, `ImportRepaperingView`.

### Registration
Both models registered in `apps/repapering/registration.py` — see that file and `apps/repapering/README.md` for full details.

---

## Project Structure
- `apps/`: Django applications.
- `eud_gui/`: Main project settings and URL configuration.
- `seeds/`: Data population scripts.
- `templates/`: Base and app-specific HTML templates.
- `static/`: Static assets (images, CSS, JS).
- `manage.py`: Standard Django entry point (customized for `--config-file`).
- `start_app.py`: Custom application launcher.
