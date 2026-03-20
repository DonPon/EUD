# Europe Domestic GUI
GUI to control the execution of bots and visualize and edit client data.
---

## Quick Start: Deploying to ADT

**Important:** To deploy the application in ADT, you **must** provide the config file path as a command-line argument using `--config-file`. If omitted, Django will default to using the local SQLite database.

```bash
python start_app.py --config-file "C:\path\to\your\config.yaml" --port 8003
```

---

## Running the Application

### Option 1: Using `start_app.py` (Recommended)
This script starts the Django development server and automatically opens your browser.

```bash
# With custom config (PostgreSQL)
python start_app.py --config-file "path/to/config.yaml" --port 8003

# Without config (defaults to SQLite)
python start_app.py --port 8003
```

**Arguments:**
- `--port`: Port to run the server on (default: 8003)
- `--config-file`: Path to YAML configuration file for database settings

> **Note:** If no `--config-file` argument is provided (in `manage.py`, `start_app.py`, or any script in `seeds/`), the application will default to using the local SQLite database.

### Option 2: Using `manage.py`
```bash
# With config file
python manage.py runserver 127.0.0.1:8003 --config-file "path/to/config.yaml"

# Without config file (uses default SQLite)
python manage.py runserver 127.0.0.1:8003
```

**Available `manage.py` commands with `--config-file` support:**
```bash
python manage.py migrate --config-file "path/to/config.yaml"
python manage.py makemigrations --config-file "path/to/config.yaml"
python manage.py shell --config-file "path/to/config.yaml"
```

### Configuration File Format
The YAML config file supports the following structure (values must be lists):

```yaml
DATABASE_TYPE:
    - 'postgres'  # Options: 'postgres' or 'sqlite'

DATABASE_NAME:
    - 'eud'

DATABASE_USER:
    - 'postgres'

DATABASE_PASSWORD:
    - 'your_password_here'

DATABASE_HOST:
    - 'localhost'

DATABASE_PORT:
    - 5432

DATABASE_SCHEMA:
    - 'public'
```

For SQLite, simply set:
```yaml
DATABASE_TYPE:
    - 'sqlite'
```

---

## Developer Guide: Extending and Modifying the System

This project is built using a **Generic CRUD Engine**. Adding new features or modifying existing data structures requires changes in three specific layers.

---

### 1. Adding a New Table (Model)

To add a new data category (e.g., "Loans" or "Credit Cards"):

#### Step A: Define the Model
Open `apps/clients/models.py` and create your class.
- **Requirement:** It MUST inherit from `ClientRelatedModel`.
```python
class Loan(ClientRelatedModel):
    loan_amount = models.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = models.FloatField()
    # client_uuid is inherited automatically
```

#### Step B: Register the Model
Open `apps/clients/registration.py` (or `apps/clients_le/registration.py` for LE models) and register the model with the engine. Inside the `register_clients_models()` function, add your registration:
- **`fields`**: List all fields for the API and the Form (include `id`, `client_uuid`, etc.).
- **`list_display`**: List only the fields you want visible in the main table (exclude UUIDs and timestamps).
- **Optional Advanced Flags:**
  - `is_client_related` (bool): Set to `False` to prevent the table from appearing on the Client Detail page (for global configurations).
  - `client_filter_field` (str): Define an alternate field to link to the Client (e.g., `'bank_rel'`). Defaults to `'client_uuid'`.
  - `read_only` (bool): Set to `True` to hide the UI buttons for adding or editing records.

```python
CrudRegistry.register(Loan, {
    'fields': ['id', 'client_uuid', 'loan_amount', 'interest_rate', 'created_at'],
    'list_display': ['loan_amount', 'interest_rate'],
    'filter_fields': ['client_uuid'],
    # 'is_client_related': False,
    # 'client_filter_field': 'bank_rel',
    # 'read_only': True
})
```

#### Step C: Database Migration
Run the standard Django commands:
```bash
python manage.py makemigrations clients
python manage.py migrate
```
**Result:** The new table will automatically appear as a section on every Client's detail page and will have its own API endpoint at `/api/table/loan/`.

---

### 2. Modifying Existing Tables (Adding/Removing Fields)

If you need to change fields in an existing table:

#### Step A: Update the Model
Modify the class in `apps/clients/models.py`.

#### Step B: Update the Registry (Crucial)
Open `apps/clients/registration.py`.
- If you **added** a field: Add it to both `fields` (to see it in the form) and `list_display` (to see it in the table).
- If you **removed** a field: Remove it from both lists, otherwise the system will throw an error trying to find it.

#### Step C: Update the Form Widgets (Optional)
If the new field is a Date or Boolean, the system handles it automatically. If you need a special dropdown (like the Portfolio dropdown in Accounts), update the `_apply_dynamic_choices` method in `apps/generic_crud/views.py`.

---

### 3. Dependency Checklist

When you change a model, ensure you check these files:

1.  **`apps/clients/models.py`**: The database structure.
2.  **`apps/clients/registration.py`**: The UI/API configuration.
3.  **`apps/generic_crud/views.py`**: Check `_get_exclude_fields` if you want to hide the new field from the user form.
4.  **`seed_data.py` / `bulk_seed.py`**: Update these if you want your test data to include the new fields.

---

### 4. UI Customization
- **Table Columns:** Managed entirely via `list_display` in `registration.py`.
- **Form Layout:** Managed automatically by `apps/generic_crud/templates/generic_crud/form.html`.
- **Audit Logs:** Automatically tracks any field added to a model inheriting from `ClientRelatedModel`.

---

### 5. Testing and Seeding Data

#### Seeding Test Data
The `seeds/` directory contains scripts to populate the database with test data:

| Script | Description |
|--------|-------------|
| `seeds/full_setup.py` | **Complete setup** - Creates admin user, generates 20 NP and LE test cases, and seeds BOTS data |
| `seeds/bulk_seed.py` | Generates bulk test data for NP and LE clients (configurable quantity) |
| `seeds/create_user.py` | Creates the admin user account |
| `seeds/seed_bots.py` | Seeds BOTS table with test data |
| `seeds/simulate_bots.py` | Simulates BOTS data runs |

**All seed scripts support the `--config-file` argument:**

```bash
# Run full setup with custom config
cd seeds
python full_setup.py --config-file "path/to/config.yaml"

# Run individual scripts with config
cd seeds
python create_user.py --config-file "path/to/config.yaml"
python bulk_seed.py --config-file "path/to/config.yaml"
python seed_bots.py --config-file "path/to/config.yaml"
python simulate_bots.py 60 --config-file "path/to/config.yaml"
```

**Run without config (defaults to SQLite):**
```bash
cd seeds
python full_setup.py
```

**Note:** Make sure the database is migrated before running seed scripts:
```bash
python manage.py migrate --config-file "path/to/config.yaml"
```

#### Running Tests
To run Django tests, use:
```bash
python manage.py test
```

---

### 6. Database Setup

#### Using SQLite (Default)
No setup required. Run the app without a config file:
```bash
python start_app.py
```

#### Using PostgreSQL
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a config file (see [Configuration File Format](#configuration-file-format)).

3. Run the app with the config file:
   ```bash
   python start_app.py --config-file "path/to/config.yaml"
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

---

### 7. Project Structure

```
EUD/
├── apps/                  # Django applications
│   ├── clients/           # Main client management app
│   ├── generic_crud/      # Generic CRUD engine
│   ├── audit/             # Audit logging
│   └── ...
├── eud_gui/               # Project settings and configuration
├── templates/             # HTML templates
├── static/                # Static files (CSS, JS, images)
├── seeds/                 # Data seeding scripts
├── manage.py              # Django management script
├── start_app.py           # Custom launcher with config support
└── config.example.yaml    # Example configuration file
```
