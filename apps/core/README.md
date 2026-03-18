# Core App (`apps/core`)

## Purpose
The `core` application serves as the foundational layer of the project. It provides abstract base models, shared logic, and global views (like the Home page) used across all other domain-specific applications.

## Most Relevant Components

### 1. `BaseUUIDModel` (`models.py`)
- **Impact:** Every record in the database (excluding default Django tables) uses a UUID as its primary key.
- **Fields:** 
  - `id`: (Primary Key, non-editable).
  - `created_at`: Timestamp of creation.
  - `updated_at`: Timestamp of the last update.

### 2. `ClientRelatedModel` (`models.py`)
- **Impact:** This is the most critical model in the system. As per the **Core Architecture Mandates**, all domain models related to the client must inherit from this.
- **Features:**
  - `client_uuid`: A UUID field used to link records to a specific client without strict database-level foreign keys, enabling horizontal scaling.
  - `history`: Automatically enables field-level audit logging via `django-simple-history`.

### 3. `HomeView` (`views.py`)
- Provides the entry point for the web application's dashboard/home interface.

## Impact of Changes

| Change | Impact |
| :--- | :--- |
| **Adding a field to `BaseUUIDModel`** | Will add that field to **every** table in the system. Requires project-wide migrations. |
| **Modifying `client_uuid` in `ClientRelatedModel`** | Could break the Generic CRUD Engine, Client Detail views, and historical data tracking. |
| **Removing `history` from `ClientRelatedModel`** | Will disable audit logging across the entire application. |

## Guidelines
- Do not add domain-specific logic here.
- Any change in `models.py` must be followed by `python manage.py makemigrations` and `python manage.py migrate` to update all dependent models.
