# Generic CRUD Engine (`apps/generic_crud`)

## Purpose
The `generic_crud` application is the "engine" of the Bank EUD project. It automates the creation of REST APIs and UI forms for domain models, drastically reducing boilerplate code. By registering a model here, you automatically get a fully functional API and a Bootstrap-ready form interface.

## Most Relevant Components

### 1. `CrudRegistry` (`registry.py`)
- **Role:** The central source of truth for all manageable models. 
- **Usage:** Models from other apps register themselves here with configurations like `fields`, `list_display`, and `search_fields`.

### 2. `DynamicSerializerFactory` (`serializers.py`)
- **Logic:** Uses Python's `type()` to generate a `serializers.ModelSerializer` class on the fly for any registered model.
- **Features:** 
    - Dynamically builds the `Meta` class based on registry config.
    - Defaults to `fields = '__all__'` if not specified.

### 3. `DynamicViewSetFactory` (`views.py`)
- **Logic:** Generates a `viewsets.ModelViewSet` for each registered model.
- **Key Features:**
    - **Automated Filtering:** Overrides `get_queryset` to automatically filter records by `client_uuid` (or custom fields like `bank_rel`).
    - **Smart Creation:** Injects the `client_uuid` from request context into new records during `perform_create`.
    - **Ordering:** Defaults to descending order by `created_at` or `date_joined`.
    - **Search/Filters:** Integrates `DjangoFilterBackend`, `OrderingFilter`, and `SearchFilter` based on registry settings.

### 4. `GenericFormView` (`views.py`)
- **Logic:** A Django `TemplateView` that uses `modelform_factory` to generate HTML forms dynamically.
- **Key Features:**
    - **Field Exclusion:** Automatically hides technical fields (UUIDs, timestamps, internal User fields).
    - **UX Enhancements:** Maps Django field types to modern HTML widgets (e.g., `<input type="date">`).
    - **Dynamic Choices:** The `_apply_dynamic_choices` method performs lookups (like filtering Portfolios by the current Client) to ensure valid data selection.
    - **Smart Redirects:** After a successful save, it intelligently redirects the user back to the Client Detail page or the User Management page.

### 5. `RoleBasedPermission` (`permissions.py`)
- **Role:** Implements the system's global access control:
    - **ADMIN:** Full CRUD.
    - **EDITOR:** View, Create, Edit (Delete is blocked).
    - **VIEWER:** Read-only (GET requests only).

## Impact of Changes

| Change | Impact |
| :--- | :--- |
| **Modifying `RoleBasedPermission`** | Changes access rights for every user and every table in the application simultaneously. |
| **Changing `GenericFormView` logic** | Affects the layout and behavior of all "Add/Edit" forms across the entire system. |
| **Updating `DynamicViewSetFactory`** | Modifies the behavior of all REST API endpoints (e.g., changing how filters or search works globally). |
| **Adding a field to the "Exclude" list** | Will hide that field from every single generic form in the project. |

## Guidelines
- Avoid adding model-specific logic directly in the factories. Instead, use the `config` dictionary in the registry to pass model-specific overrides.
- When adding a new feature to the generic UI, ensure it remains compatible with standard Bootstrap 5 and the `client_uuid` architectural pattern.
