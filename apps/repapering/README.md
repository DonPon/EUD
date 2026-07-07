# Repapering Module

The Repapering module defines **document requirement scenarios** — mappings between banking scenarios (e.g., "A - Natural Person Resident") and the documents needed for each. It serves as the single source of truth consumed by the core banking logic.

---

## Data Models

### Scenario
| Field  | Type           | Description                                    |
|--------|----------------|------------------------------------------------|
| `id`   | UUID (PK)      | Auto-generated primary key                     |
| `name` | `CharField`    | Human-readable name, e.g. "A - Natural Person" |

Relations:
- Has many `DocumentRequirement` records via `requirements` reverse relation.
- History tracked via `django-simple-history`.

### DocumentRequirement
| Field                   | Type           | Description                                           |
|-------------------------|----------------|-------------------------------------------------------|
| `id`                    | UUID (PK)      | Auto-generated primary key                            |
| `scenario`              | `ForeignKey`   | Parent `Scenario` (CASCADE delete)                    |
| `cdok`                  | `CharField`    | Document code (CDOK) identifier                       |
| `duplicate`             | `BooleanField` | Whether the document can be duplicated                |
| `granularity`           | `CharField`    | One of: `One for each Co-owner`, `One for each BO`, `One for each LR`, `One for each POA` |
| `output_folder_structure` | `CharField`  | Path template for output folder                       |
| `pdf_template`          | `FileField`    | Uploaded PDF template file (stored under `repapering_templates/`) |

Relations:
- Belongs to exactly one `Scenario`.
- History tracked via `django-simple-history`.

---

## UI Workflow

1. **Scenario List** (`/repapering/`) — lists all scenarios with a "View / Map Docs" button
2. **Scenario Detail** (`/repapering/scenario/<id>/`) — shows mapped documents for a scenario
   - "Add Document Mapping" — creates a new `DocumentRequirement` linked to the scenario
   - "Edit Scenario" / "Edit Document" — opens the Generic CRUD form
   - Delete — removes a `DocumentRequirement` (also deletes its PDF template)
3. **Create/Edit forms** — rendered by the Generic CRUD engine; `scenario` FK is pre-selected via GET parameter

---

## Permissions

| Role     | Scenario List | Scenario Detail | Add / Edit / Delete | Export JSON | Import JSON |
|----------|:------------:|:---------------:|:-------------------:|:-----------:|:-----------:|
| ADMIN    | ✓            | ✓               | ✓                   | ✓           | ✓           |
| EDITOR   | ✓            | ✓               | ✓                   | ✗           | ✗           |
| VIEWER   | ✓            | ✓               | ✗                   | ✗           | ✗           |

Export and Import views enforce `AdminRequiredMixin`; all mutation views enforce `EditorOrAdminRequiredMixin`.

---

## Import / Export

Export downloads all scenarios and their document requirements as a JSON file (`repapering_settings.json`). Import reads a JSON file and performs an atomic upsert — scenarios are matched by name, and their requirements are fully replaced.

**Only ADMIN users** can export or import.

---

## PDF Template Management

- Templates are uploaded via the `DocumentRequirement` form (as `FileField`).
- When a template is **replaced**, the old file is automatically deleted from storage (handled by `pre_save` signal in `signals.py`).
- When a `DocumentRequirement` is **deleted**, its template file is also removed (handled by `post_delete` signal).
- PDF templates are served directly via Django's static file serving.

---

## Audit Logging

All changes to `Scenario` and `DocumentRequirement` are tracked with `django-simple-history`:
- `repapering_historicalscenario`
- `repapering_historicaldocumentrequirement`

Each historical record stores the timestamp and the user who made the change.

---

## Developer Guide

### Registering Models

Both models are registered in `apps/repapering/registration.py` via the Generic CRUD engine:

```python
CrudRegistry.register(Scenario, {
    'section': 'repapering',
    'fields': ['id', 'name'],
    'list_display': ['name'],
    'search_fields': ['name'],
    'cancel_url_name': 'repapering:scenario_list',
})

CrudRegistry.register(DocumentRequirement, {
    'section': 'repapering',
    'fields': ['id', 'scenario', 'cdok', 'duplicate', 'granularity',
               'output_folder_structure', 'pdf_template'],
    'list_display': ['scenario', 'cdok', 'duplicate', 'granularity', 'pdf_template'],
    'search_fields': ['cdok', 'scenario__name'],
    'filter_fields': ['scenario', 'duplicate', 'granularity'],
    'cancel_url_name': 'repapering:scenario_detail',
})
```

### Adding / Removing Fields

1. Update the model in `apps/repapering/models.py`
2. Update `fields` and `list_display` in `apps/repapering/registration.py`
3. Run migrations
4. If the new field needs a dynamic dropdown, add logic to `_apply_dynamic_choices` in `apps/generic_crud/views.py`

### Custom Views

The app uses custom class-based views (not generic CRUD) for:
- `ScenarioListView` — scenario listing page
- `ScenarioDetailView` — detail page with document mappings table
- `DocumentRequirementDeleteView` — custom delete with redirect back to scenario detail
- `ExportRepaperingView` / `ImportRepaperingView` — JSON export/import

### Signals

Defined in `apps/repapering/signals.py`:
- `delete_pdf_file` — `post_delete` on `DocumentRequirement`
- `cleanup_old_pdf` — `pre_save` on `DocumentRequirement` (replaces old file)
