# GEMINI.md - Bank EUD Project

## 1. Project Mission
A highly scalable, production-grade Django web application designed for a banking environment. The system manages complex client data across multiple decoupled tables using a central `client_uuid` concept. Provide robust auditing, generic forms, and REST APIs powered by the Django REST Framework.

## 2. Core Architecture Mandates

### 2.1. Client-Centric Data Model
- **Shared UUID:** Tables are linked by a `client_uuid` field, NOT necessarily by hard database-level foreign keys. This allows for horizontal scaling and independent table evolution.
- **Base Models:** All models MUST inherit from `apps.core.models.ClientRelatedModel`.
- **UUID Primary Keys:** All records use UUIDs as their primary key (`id`).
- **Global Entities:** Models not strictly bound to a single client (e.g. bots or global configurations) should override the save method to default `client_uuid` to a zero-UUID (`00000000-0000-0000-0000-000000000000`).

### 2.2. Generic CRUD Engine (`apps/generic_crud`)
The system uses a **Registry Pattern** to automate boilerplate tasks.
- **Registry:** `apps/generic_crud/registry.py`. All domain models must be registered here.
- **Dynamic API:** ViewSets and Serializers are generated on-the-fly based on registry config using Django REST Framework (DRF).
- **Generic Forms:** `GenericFormView` automatically renders Bootstrap 5 forms and handles automated `client_uuid` injection during saves.
- **Advanced Config:** The registry supports flags like `is_client_related` (to decouple global models from the Client UI), `read_only` (to disable Add/Edit form UI), and `client_filter_field` (to relate records via alternate constraints like `bank_rel`).

### 2.3. Audit Logging
- **Simple History:** Every model must use `HistoricalRecords(inherit=True)` from `django-simple-history`.
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
- **Forms:** Leverage Bootstrap 5 form controls globally, provided primarily by the generic forms implementation.

## 4. App Directory
- `apps/core`: Abstract base models and shared logic.
- `apps/users`: Custom `User` model and role management.
- `apps/clients`: Banking domain models (e.g. internal representations of accounts) and the model registration file.
- `apps/dashboard_bots`: Models for tracking RPA bot configurations, statuses, and execution records relative to banking clients.
- `apps/generic_crud`: The engine (Registry, Dynamic ViewSets, Generic Forms).
- `apps/audit`: Historical data calculation and audit UI.

## 5. Development Setup
```bash
python -m venv venv
source venv/bin/activate # Linux
pip install -r requirements.txt
python manage.py migrate
```

### 5.1. Seeding Data
Choose the appropriate script to seed your local database:
- `python seeds/seed_data.py`: Creates Admin user and a sample Bank Client.
- `python seeds/bulk_seed.py`: Generates larger volumes of test clients via the Faker library.
- `python seeds/seed_bots.py`: Seeds initial bot reference data and execution records.
- `python seeds/simulate_bots.py <seconds>`: Runs a real-time activity simulation for the bots dashboard.

```bash
python manage.py runserver
```
