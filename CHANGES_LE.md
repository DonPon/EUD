## Changes Required for "clients_le"

Perform these following changes for the models in the app "clients_le". These changes are ONLY intended for the app "clients_le".

Make sure to also edit the registration if needed.

Please check the checkbox in this document when a change is done, so we could continue where we left.

When renaming verbose name, if needed, rename the actual name of the fields to fit more appropriate to the new names.

### TABLE: Banking Relationship Information
- [ ] **RENAME:** `Client Segment Code (Csc)` $\rightarrow$ `CSC` 
- [ ] **REMOVE:** `ID Copy Provided` 
- [ ] **REMOVE CHOICES:** From `Client Segment > Dropdown list` $\rightarrow$ Remove `120`, `131`, `132` 
- [ ] **ADD CHOICES:** To `Client Segment > Dropdown list` $\rightarrow$ Add `241`, `244`, `243`, `231`, `220`, `233`, `232`, `270`, `266` 

### Table: company information
- [ ] **ADD:** `Fiduciary mandate (new field) (Yes; no)` 

### Table: communication
- [ ] **RENAME:** Under `Type` $>$ `Choices` $\rightarrow$ Rename `Telephone` to `Fixed Number` 
- [ ] **RENAME VERBOSE NAME:** Field `address` $\rightarrow$ Rename to `Address (email)` 

### Table: relationship
- [ ] **RENAME VERBOSE NAME:** `Technical Account` $\rightarrow$ `BR-Technical Account` 
- [ ] **ADD:** Inside `Relationship` dropdown $\rightarrow$ Add `POA (Information)` 
- [ ] **ADD:** Add `signature type` in details 

### Table: Products
- [ ] **REMOVE:** `ALTERNATIVE INVESTMENT` 
- [ ] **REMOVE:** `CURRENCY HEDGING` 
- [ ] **REMOVE:** `SHARE FOCUS` 