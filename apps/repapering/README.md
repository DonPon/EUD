# Repapering Module

The Repapering module uses the **Django Database** as the single source of truth for all scenario definitions and document requirements.

## Workflow
1. Users make changes via the EUD Repapering interface.
2. The core banking logic reads the database directly to apply rules.

## Audit Logs
All modifications made via the UI are tracked using `django-simple-history`. Database tables `repapering_historicalscenario` and `repapering_historicaldocumentrequirement` store the exact timestamps and authors of any changes.
