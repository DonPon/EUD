# Prompt: Django Model Refactor - Star Schema Migration

**Context:**
I am refactoring the existing Django-based Banking GUI from this project. I need to implement a "Star Schema" where a central `client_uuid` acts as the logical connector for all data. I have two existing models, `Portfolio` and `Account`, which must be preserved and updated to link to this new structure. The rest of the models should be modified according to the instructions.

**Strict Architectural Rules:**
1. **The Hub:** Every model must include a `client_uuid = UUIDField(db_index=True)` as right now.
2. **No Django M2M:** Do not use `ManyToManyField`. All complex relationships are handled by the `Relationship` model (Model 12) acting as an Edge Table. This table will link one main client together with another person for example a "POA" or when a joint-account this should link all the co-owners, etc. should manage all relashonships the client has with other persons or companies (which is something new in the GUI).
3. **Primary Keys:** Keep standard Django `id` as the technical PK, but all logical associations must use `client_uuid`.
4. **Data Integrity:** Use `JSONField` for multi-select data to keep the schema flat and avoid extra join tables.

---

### **New Model Specifications**

#### **1. BankingRelationship (Root/Hub)**
* **Fields:** `client_uuid` (Indexed), `banking_relationship` (Char), `technical_account` (Bool), `additional_br` (Char), `distribution_list` (Char), `name_of_banking_relationship` (Char), `type_of_account` (Choices: 120, 131, 132), `type_of_signature` (Choices: Joint, Disjoint), `client_segment` (Choices: CORA, HNWI), `code_ksc` (Choices: 541, 543, 546, 548, 561, 563, 566, 568), `recording_phone_calls` (Bool), `declaration_email` (Email), `language` (Choices: German, English, Spanish), `opened_in_ubs_premises` (Bool), `instructions` (Text), `account_and_securities_statements` (JSONField: Monthly, Additional on a daily basis, Collective settlement), `type_and_purpose` (JSONField: Payment transactions, Asset/Cash investment, Credit Business, Other), `agreement_distribution_fees` (Choices: Normal case, Complete payout, Partial payout), `send_documents` (JSONField: To client, To CA, Digitally), `csc`, `ateco`, `sae`, `level_of_professionalism` (Int), `number_of_portfolios` (Int).

#### **2. AdditionalFormDE (Regulatory/Tax)**
* **Fields:** `client_uuid`, `request_to_become_professional` (Bool), `forward_trading_transactions` (Bool), `exemption_order` (Bool), `last_name`, `first_name`, `name_at_birth`, `street`, `no`, `postal_code`, `city`, `country`, `identification_number`, `date_of_birth` (Date), `amount` (Choices: Up to an amount of (EUR), Up to the total savers allowance, Over EUR 0), `timeline` (Choices: Until 31 December, As long as you have received another amount, This order is valid as of, Or from the start of the business relationship), `date_until` (Date), `valid_as_of` (Date), `standing_order_form` (Bool), `execution` (Choices: Weekly, Every 2 weeks, Monthly, Every 2 months, Every 3 months, Every 4 months, Every 6 months, Annually), `day_of_execution` (Int), `month` (Int), `year` (Int), `until_canceled` (Bool), `limited_power_of_attorney` (Bool), `poa_all_accounts` (Bool), `poa_in_case_of_death` (Bool), `tax_at_source_canada` (Bool), `ubs_digital_banking_authorization` (Bool).

#### **3. PersonalInformation**
* **Fields:** `client_uuid`, `first_name`, `last_name`, `name_at_birth`, `federal_state`, `date_of_birth` (Date), `place_of_birth`, `country_of_birth`, `marital_status`, `occupation_sector`, `fiscal_identifier`, `indication_tin`, `sensitive_client` (Bool).

#### **4. Address (1:N)**
* **Fields:** `client_uuid`, `person_entity`, `type_of_address` (Choices: Domicile, Correspondence, Third party, Tax domicile, Fiscal residence), `first_name`, `last_name`, `c_o`, `street`, `no`, `postal_code`, `city`, `province`, `country`, `documents_sent` (Bool).

#### **5. Communication (1:N)**
* **Fields:** `client_uuid`, `first_and_last_name`, `landline`, `phone` (Choices: Work, Private), `phone_number`, `mobile_work` (Choices: Work, Private), `mobile_number`, `email` (Choices: Work, Private), `email_address` (EmailField), `fax` (Choices: Work, Private), `fax_address`, `pec_address`.

#### **6. ClientAdvisor (1:N)**
* **Fields:** `client_uuid`, `first_name`, `last_name`, `email` (EmailField), `desk`, `branch`, `role` (Choices: Requestor, Client Advisor, Deputy Client Advisor).

#### **7. Nationality (1:N)**
* **Fields:** `client_uuid`, `is_main_nationality` (Bool), `nationality`, `nci`, `id_type`, `fiscal_code`, `fiscal_code_path`, `release_authority`, `release_location`, `release_date` (Date), `expiry_date` (Date), `is_id_document_provided` (Bool), `id_document_path`.

#### **8. TIN (Tax ID - 1:N)**
* **Fields:** `client_uuid`, `aei_tin`.

#### **9. EBanking (1:N)**
* **Fields:** `client_uuid`, `has_ebanking` (Bool), `contract_number`.

#### **10. Product (1:N)**
* **Fields:** `client_uuid`, `product_name`, `product_id`, `status`.

#### **11. MeetingPreparation (1:N)**
* **Fields:** `client_uuid`, `place` (Choices: Internal, External), `number_of_participants` (Int), `date_of_meeting` (Date), `time` (Time), `room_booking` (Bool), `hospitality` (Choices: None, Cold drinks, coffee or tea on request, Breakfast, Lunch), `technical_equipment_needed` (Bool), `performance_since_beginning` (Decimal), `performance_before_tax` (Decimal), `performance_since_start` (Decimal), `investor_profile_link` (URL), `email_waiver` (Bool).

#### **12. Relationship (The Edge Table / Graph)**
* **Fields:** `client_uuid` (Source), `child_unique_id` (Target Identifier), `type_of_relationship`, `type_of_access`, `level_of_access` (JSONField: Limited Power of attorney, Power of attorney for all accounts, Power of attorney in the event of death, Power of attorney to reclaim tax at source), `relation_with_owner`.

---

### **Action Plan for the Agent:**
0. First explain what is needed to change and make sure you understand the task.
1. **Update models.py:** Implement the structures above.
2. **Preserve Existing Data:** Preserve `Portfolio` and `Account` models.
3. **Defaults:** Ensure all `CharField` and `JSONField` have appropriate defaults (e.g., `blank=True` or `default=list`) to avoid migration issues.
4. **Migrations:** Do NOT Generate the migration files yet.
