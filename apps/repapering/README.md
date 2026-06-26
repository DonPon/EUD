# Repapering Configuration Guide

The Repapering module uses a structured JSON file (`repapering_config.json`) as its source of truth for logic and rules. The Django database models serve as a UI wrapper to manage mappings and PDFs easily.

## Config File Structure
The file is structured as follows:
```json
{
    "scenarios": [
        {
            "scenario_id": "A_NP_RES",
            "name": "A - Natural Person Resident",
            "description": "Rules for Resident Natural Persons."
        }
    ],
    "document_requirements": [
        {
            "scenario_id": "A_NP_RES",
            "cdok": "ID_CARD",
            "duplicate": false,
            "granularity": "One per client",
            "output_folder_structure": "01_ID",
            "input_filename": "ID_Document.pdf",
            "pdf_template": "repapering_templates/template.pdf",
            "rules_special_conditions": "Required if Age >= 18"
        }
    ]
}
```

## How It Works
1. When changes are made via the EUD Repapering interface, a Django signal automatically updates `repapering_config.json`.
2. The core banking logic reads this `repapering_config.json` to decide which documents are required for specific scenarios based on the `rules_special_conditions`.
3. Rules logic evaluates the `rules_special_conditions` string (e.g. `ClientType == 'NP' and Resident == True`). The UI displays this logic as View-Only to ensure business analysts don't accidentally break complex technical conditions.

## Version Control
We strongly recommend committing `repapering_config.json` into Git.
```bash
git add repapering_config.json
git commit -m "Update repapering rules for ID Cards"
```
This ensures all logic changes are tracked and can be safely deployed or rolled back.

## Audit Logs
All modifications made via the UI are tracked using `django-simple-history`. Database tables `repapering_historicalscenario` and `repapering_historicaldocumentrequirement` store the exact timestamps and authors of any changes.
