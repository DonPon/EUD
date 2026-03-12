# GEMINI.md - Bank EUD Project

## 1. Project Mission
A highly scalable, production-grade Django web application designed for a banking environment. The system manages complex client data across multiple decoupled tables using a central `client_uuid` concept.

## 2. Core Architecture Mandates

### 2.1. Client-Centric Data Model
- **Shared UUID:** Tables are linked by a `client_uuid` field, NOT necessarily by hard database-level foreign keys. This allows for horizontal scaling and independent table evolution.
- **Base Models:** All models MUST inherit from `apps.core.models.ClientRelatedModel`.
- **UUID Primary Keys:** All records use UUIDs as their primary key (`id`).

### 2.2. Generic CRUD Engine (`apps/generic_crud`)
The system uses a **Registry Pattern** to automate boilerplate tasks.
- **Registry:** `apps/generic_crud/registry.py`. All domain models must be registered here.
- **Dynamic API:** ViewSets and Serializers are generated on-the-fly based on registry config.
- **Generic Forms:** `GenericFormView` automatically renders Bootstrap 5 forms and handles automated `client_uuid` injection during saves.

### 2.3. Audit Logging
- **Simple History:** Every model must use `HistoricalRecords(inherit=True)`.
- **Custom Audit UI:** The system provides a full-page, paginated history view (`apps/audit`) that calculates field-level deltas (Old Value -> New Value).

## 3. Engineering Standards

### 3.1. Adding a New Table
To add a new data category (e.g., "Loans"):
1.  **Model:** Define `Loan` in `apps/clients/models.py` inheriting from `ClientRelatedModel`.
2.  **Registration:** Add `CrudRegistry.register(Loan, {...})` in `apps/clients/registration.py`.
3.  **UI:** The table will automatically appear as a section on the Client Detail page.

### 3.2. Role-Based Access Control (RBAC)
- **ADMIN:** Full CRUD + History.
- **EDITOR:** View, Create, Edit. **Delete is prohibited.**
- **VIEWER:** Read-only access. All "Add/Edit" buttons are hidden from the UI.

### 3.3. UI/UX Rules
- **Hidden Technicals:** Internal IDs (UUIDs) and `created_at` timestamps MUST be hidden from main tables. They are only visible via the "Technical Details" modal.
- **DataTables:** Use the `initDataTable` wrapper in `base.html`. Only CSV export is permitted (Copy/Excel removed).
- **Date Inputs:** Always use native `<input type="date">` via the `DateInput` widget.

## 4. App Directory
- `apps/core`: Abstract base models and shared logic.
- `apps/users`: Custom `User` model and role management.
- `apps/clients`: Banking domain models and the model registration file.
- `apps/generic_crud`: The engine (Registry, Dynamic ViewSets, Generic Forms).
- `apps/audit`: Historical data calculation and audit UI.

## 5. Development Setup
```bash
python -m venv venv
source venv/bin/activate # Linux
pip install -r requirements.txt
python manage.py migrate
python seed_data.py # Creates Admin and sample Bank Client
python manage.py runserver
```
