## Changes Required for "clients_le"

Perform these following changes for the models in the app "clients_le". These changes are ONLY intended for the app "clients_le".

Make sure to also edit the registration if needed.

Please check the checkbox in this document when a change is done, so we could continue where we left.

When renaming verbose name, if needed, rename the actual name of the fields to fit more appropriate to the new names.

### TABLE: Banking Relationship Information
- [x] **RENAME:** `Client Segment Code (Csc)` $\rightarrow$ `CSC` 
- [x] **REMOVE:** `ID Copy Provided` 
- [x] **REMOVE CHOICES:** From `Client Segment > Dropdown list` $\rightarrow$ Remove `120`, `131`, `132` 
- [x] **ADD CHOICES:** To `Client Segment > Dropdown list` $\rightarrow$ Add `241`, `244`, `243`, `231`, `220`, `233`, `232`, `270`, `266` 

### Table: company information
- [x] **ADD:** `Fiduciary mandate (new field) (Yes; no)` 

### Table: communication
- [x] **RENAME:** Under `Type` $>$ `Choices` $\rightarrow$ Rename `Telephone` to `Fixed Number` 
- [x] **RENAME VERBOSE NAME:** Field `address` $\rightarrow$ Rename to `Address (email)` 

### Table: relationship
- [x] **RENAME VERBOSE NAME:** `Technical Account` $\rightarrow$ `BR-Technical Account` 
- [x] **ADD:** Inside `Relationship` dropdown $\rightarrow$ Add `POA (Information)` 
- [x] **ADD:** Add `signature type` in details 

### Table: Products
- [x] **REMOVE:** `ALTERNATIVE INVESTMENT` 
- [x] **REMOVE:** `CURRENCY HEDGING` 
- [x] **REMOVE:** `SHARE FOCUS` 


---- 
OUTPUTS
✦ I have completed the changes for the clients_le app as specified in CHANGES_LE.md.

  Summary of Changes:

  Banking Relationship Information (LE_BankingRelationship)
   * Renamed code_csc field to csc and updated its verbose name to "CSC".
   * Removed the id_doc_provided field.
   * Updated SEGMENT_TYPE_CHOICES by removing 120, 131, 132 and adding 241, 244, 243, 231, 220, 233, 232, 270, 266.
   * Updated the registration in apps/clients_le/registration.py to reflect these changes.

  Company Information (LE_Company)
   * Added a new field fiduciary_mandate with "Yes/No" choices.
   * Updated the registration to include the new field and added it to filter_fields.

  Communication (LE_Communication)
   * Renamed the "Telephone" choice to "Fixed Number" in TYPE_CHOICES.
   * Changed the verbose_name of the address field to "Address (email)".

  Relationship (LE_Relationship)
   * Renamed the verbose_name of technical_account to "BR-Technical Account".
   * Added "POA (Information)" to RELATIONSHIP_CHOICES.
   * Added a new field signature_type and updated the registration.

  Products (LE_Product)
   * Removed alternative_investment, currency_hedging, and share_focus fields from the model and registration.

  All items in CHANGES_LE.md have been checked off. Please note that I have not run migrations as per the project instructions.