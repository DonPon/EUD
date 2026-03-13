# Developer Guide: Extending and Modifying the Bank EUD System

This project is built using a **Generic CRUD Engine**. Adding new features or modifying existing data structures requires changes in three specific layers.

---

## 1. Adding a New Table (Model)

To add a new data category (e.g., "Loans" or "Credit Cards"):

### Step A: Define the Model
Open `apps/clients/models.py` and create your class.
- **Requirement:** It MUST inherit from `ClientRelatedModel`.
```python
class Loan(ClientRelatedModel):
    loan_amount = models.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = models.FloatField()
    # client_uuid is inherited automatically
```

### Step B: Register the Model
Open `apps/clients/registration.py` and register the model with the engine.
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

### Step C: Database Migration
Run the standard Django commands:
```bash
python manage.py makemigrations clients
python manage.py migrate
```
**Result:** The new table will automatically appear as a section on every Client's detail page and will have its own API endpoint at `/api/table/loan/`.

---

## 2. Modifying Existing Tables (Adding/Removing Fields)

If you need to change fields in an existing table:

### Step A: Update the Model
Modify the class in `apps/clients/models.py`.

### Step B: Update the Registry (Crucial)
Open `apps/clients/registration.py`.
- If you **added** a field: Add it to both `fields` (to see it in the form) and `list_display` (to see it in the table).
- If you **removed** a field: Remove it from both lists, otherwise the system will throw an error trying to find it.

### Step C: Update the Form Widgets (Optional)
If the new field is a Date or Boolean, the system handles it automatically. If you need a special dropdown (like the Portfolio dropdown in Accounts), update the `_apply_dynamic_choices` method in `apps/generic_crud/views.py`.

---

## 3. Dependency Checklist

When you change a model, ensure you check these files:

1.  **`apps/clients/models.py`**: The database structure.
2.  **`apps/clients/registration.py`**: The UI/API configuration.
3.  **`apps/generic_crud/views.py`**: Check `_get_exclude_fields` if you want to hide the new field from the user form.
4.  **`seed_data.py` / `bulk_seed.py`**: Update these if you want your test data to include the new fields.

---

## 4. UI Customization
- **Table Columns:** Managed entirely via `list_display` in `registration.py`.
- **Form Layout:** Managed automatically by `apps/generic_crud/templates/generic_crud/form.html`.
- **Audit Logs:** Automatically tracks any field added to a model inheriting from `ClientRelatedModel`.
