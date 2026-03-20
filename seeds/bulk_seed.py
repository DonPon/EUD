import os
import sys
import django
import uuid
import random
import argparse
from datetime import date, timedelta
from pathlib import Path
from faker import Faker

# Parse config-file argument if present
parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("--config-file", type=str, default="")
args, remaining = parser.parse_known_args()

# Store config file path in environment variable for settings.py to use
if args.config_file:
    os.environ["EUD_CONFIG_FILE"] = args.config_file

# Add the project root to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eud_gui.settings')
django.setup()

from apps.users.models import User
from apps.clients.models import (
    BankingRelationship, AdditionalFormDE, PersonalInformation, Address,
    Communication, ClientAdvisor, Nationality, TIN, EBanking,
    Product, MeetingPreparation, Relationship, Account
)
from apps.clients_le.models import (
    LE_BankingRelationship, LE_PersonalInformation, LE_Company, LE_Address, LE_Communication,
    LE_ClientAdvisor, LE_Nationality, LE_TIN, LE_EBanking, LE_MeetingPreparation,
    LE_Product, LE_Account, LE_Relationship
)

fake = Faker()

def bulk_seed(num_clients=20, num_le_clients=10):
    print(f"Starting bulk seed of {num_clients} NP and {num_le_clients} LE banking relationships...")

    status_options = ['pending_review', 'ready_for_bot_1', 'ready_for_bot_2', 'ready_for_bot_3','ready_for_bot_4', 'ready_for_bot_5', 'ready_for_bot_6', 'ready_for_bot_7', 'ready_for_bot_8', 'completed']

    # --- Seed Natural Person (NP) Clients ---
    all_client_uuids = []
    for i in range(num_clients):
        client_uuid = uuid.uuid4()
        all_client_uuids.append(client_uuid)
        
        # 1. Create BankingRelationship (The Hub)
        br = BankingRelationship.objects.create(
            client_uuid=client_uuid,
            banking_relationship=f"BR-{random.randint(100000, 999999)}",
            technical_account=random.choice([True, False]),
            additional_br=f"ADD-{random.randint(1000, 9999)}",
            distribution_list=fake.word(),
            name_of_banking_relationship=fake.company(),
            type_of_account=random.choice(['120', '131', '132']),
            type_of_signature=random.choice(['Joint', 'Disjoint']),
            client_segment=random.choice(['CORA', 'HNWI']),
            code_ksc=random.choice(['541', '543', '546', '548', '561', '563', '566', '568']),
            recording_phone_calls=random.choice([True, False]),
            declaration_email=fake.email(),
            language=random.choice(['German', 'English', 'Spanish']),
            opened_in_ubs_premises=random.choice([True, False]),
            instructions=fake.paragraph(),
            status=random.sample(status_options, k=random.randint(0, 3)),
            account_and_securities_statements=random.sample(['Monthly', 'Collective settlement', 'Additional on a daily basis'], k=random.randint(1, 2)),
            type_and_purpose=random.sample(['Payment transactions', 'Asset/Cash investment', 'Credit Business', 'Other'], k=random.randint(1, 2)),
            agreement_distribution_fees=random.choice(['Normal case', 'Complete payout', 'Partial payout']),
            send_documents=random.sample(['To client', 'To CA', 'Digitally'], k=random.randint(1, 2)),
            csc=fake.bothify(text='CSC-####'),
            ateco=fake.bothify(text='ATECO-####'),
            sae=fake.bothify(text='SAE-####'),
            level_of_professionalism=random.randint(1, 5),
            number_of_portfolios=random.randint(1, 10)
        )

        # 2. Create AdditionalFormDE
        AdditionalFormDE.objects.create(
            client_uuid=client_uuid,
            request_to_become_professional=random.choice([True, False]),
            forward_trading_transactions=random.choice([True, False]),
            exemption_order=random.choice([True, False]),
            last_name=fake.last_name(),
            first_name=fake.first_name(),
            identification_number=fake.ssn(),
            date_of_birth=fake.date_of_birth(minimum_age=18, maximum_age=90),
            amount=random.choice(['Up to an amount of (EUR)', 'Up to the total savers allowance', 'Over EUR 0']),
            timeline=random.choice(['Until 31 December', 'This order is valid as of', 'Or from the start of the business relationship']),
            execution=random.choice(['Weekly', 'Monthly', 'Annually']),
            day_of_execution=random.randint(1, 28),
            until_canceled=random.choice([True, False]),
            limited_power_of_attorney=random.choice([True, False]),
            ubs_digital_banking_authorization=random.choice([True, False])
        )

        # 3. Create PersonalInformation
        PersonalInformation.objects.create(
            client_uuid=client_uuid,
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            date_of_birth=fake.date_of_birth(minimum_age=18, maximum_age=90),
            place_of_birth=fake.city(),
            country_of_birth=fake.country(),
            marital_status=random.choice(['Single', 'Married', 'Divorced']),
            occupation_sector=fake.job(),
            fiscal_identifier=fake.bothify(text='FISCAL-#######'),
            sensitive_client=random.choice([True, False])
        )

        # 4. Create Addresses
        for _ in range(random.randint(1, 3)):
            Address.objects.create(
                client_uuid=client_uuid,
                person_entity=fake.name(),
                type_of_address=random.choice(['Domicile', 'Correspondence', 'Tax domicile']),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                street=fake.street_address(),
                no=fake.building_number(),
                postal_code=fake.zipcode(),
                city=fake.city(),
                country=fake.country(),
                documents_sent=random.choice([True, False])
            )

        # 5. Create Communications
        for _ in range(random.randint(1, 4)):
            Communication.objects.create(
                client_uuid=client_uuid,
                first_and_last_name=fake.name(),
                phone=random.choice(['Work', 'Private']),
                phone_number=fake.phone_number(),
                email=random.choice(['Work', 'Private']),
                email_address=fake.email(),
                fax_address=fake.phone_number() if random.choice([True, False]) else ""
            )

        # 6. Create ClientAdvisor
        ClientAdvisor.objects.create(
            client_uuid=client_uuid,
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.company_email(),
            branch=fake.city(),
            role=random.choice(['Client Advisor', 'Deputy Client Advisor'])
        )

        # 7. Create Nationalities
        for _ in range(random.randint(1, 2)):
            Nationality.objects.create(
                client_uuid=client_uuid,
                is_main_nationality=(_ == 0),
                nationality=fake.country(),
                id_type=random.choice(['Passport', 'ID Card', 'Driver License']),
                expiry_date=fake.future_date(end_date="+5y")
            )

        # 8. Create TIN, EBanking
        TIN.objects.create(client_uuid=client_uuid, aei_tin=fake.bothify(text='TIN-#########'))
        EBanking.objects.create(client_uuid=client_uuid, has_ebanking=random.choice([True, False]), contract_number=fake.bothify(text='EB-########'))
        
        # 9. Create Products and Accounts
        for _ in range(random.randint(1, 5)):
            product_obj = Product.objects.create(
                client_uuid=client_uuid,
                portfolio_id=fake.bothify(text='PORT-####'),
                portfolio_name=fake.company() + " Portfolio",
                email_waiver=random.choice([True, False]),
                reference_currency=random.choice(['USD', 'EUR', 'GBP', 'CHF']),
                investment_service=random.choice(['Asset Management', 'Wealth Management', 'Advisory']),
                a_s_authorization_path=f"/path/to/auth/{fake.word()}.pdf",
                investment_strategy=random.choice(['Conservative', 'Balanced', 'Growth', 'Aggressive']),
                ip_risk_tolerance=random.choice(['Low', 'Medium', 'High']),
                investment_amount=random.uniform(10000.0, 1000000.0),
                selected_service=random.choice(['Basic', 'Premium', 'Elite']),
                all_in=random.choice([True, False]),
                sustainable_investing=random.choice([True, False]),
                sustainability_preference=random.choice(['Environmental', 'Social', 'Governance']),
                focus_equity=random.choice([True, False]),
                alternative_investment=random.choice([True, False]),
                direct_instrument=random.choice([True, False]),
                initial_amount=random.uniform(5000.0, 500000.0),
                foreign_hedging=random.choice(['Discretion of UBS', 'None for share allocation']),
                transaction_confirmation=random.choice([True, False]),
                empty_kyc_form_path=f"/path/to/kyc/{fake.word()}.pdf",
                investor_profile_path=f"/path/to/profile/{fake.word()}.pdf",
                myway_module_path=f"/path/to/myway/{fake.word()}.pdf",
                ntac=random.choice(['Excluded', 'Permitted']),
                reporting_loss=random.choice(['Monthly', 'Quarterly']),
                share_focus=random.choice(['EMU: Predominantly...', 'Global equity...']),
                date_of_alignment=fake.date_between(start_date='-1y', end_date='today'),
                end_date_alignment=fake.date_between(start_date='today', end_date='+1y'),
                type_of_business_settlement=random.choice(['Monthly', 'Individual']),
                special_conditions=fake.paragraph(),
                discount_applied=random.choice([True, False]),
                discount_amount_percent=random.uniform(0.0, 50.0),
                flat_fee_applied=random.choice([True, False]),
                flat_fee_percent=random.uniform(0.1, 2.0),
                invested_assets=random.uniform(100000.0, 5000000.0),
                income_pa=random.uniform(1000.0, 50000.0),
                current_return_on_assets=random.uniform(0.01, 0.10),
                target_roa=random.uniform(0.05, 0.15),
                net_new_money_potential=random.uniform(0.0, 1000000.0),
                business_case_communication=random.choice(['Option 1 (in person)', 'Option 2 (online)']),
                fee_model='Advice plus transaction fee',
                mandate_fee=random.choice([True, False]),
                service_and_execution=random.choice(['UBS Manage', 'UBS Advice']),
                no_discount=random.choice([True, False]),
                no_discount_amount_percent=random.uniform(0.0, 10.0),
                no_flat_fee=random.choice([True, False]),
                no_flat_fee_amount=random.uniform(100.0, 1000.0),
                transaction_fee=random.uniform(10.0, 100.0),
                standard_fee_discount=random.uniform(0.0, 20.0),
                shares_fee=random.choice([True, False]),
                shares_fee_amount=random.uniform(50.0, 500.0),
                shares_discount=random.choice([True, False]),
                shares_discount_amount=random.uniform(10.0, 100.0),
                investment_funds_fee=random.choice([True, False]),
                investment_fund_fee_amount=random.uniform(50.0, 500.0),
                investment_fund_discount=random.choice([True, False]),
                investment_fund_discount_amount=random.uniform(10.0, 100.0),
                fixed_income_fee=random.choice([True, False]),
                fixed_income_fee_amount=random.uniform(50.0, 500.0),
                fixed_income_discount=random.choice([True, False]),
                fixed_income_discount_amount=random.uniform(10.0, 100.0),
                fixed_income_investment_funds_fee=random.choice([True, False]),
                fixed_income_investment_funds_fee_amount=random.uniform(50.0, 500.0),
                fixed_income_investment_funds_discount=random.choice([True, False]),
                fixed_income_investment_funds_discount_amount=random.uniform(10.0, 100.0),
                shares_investment_funds_fee=random.choice([True, False]),
                shares_investment_funds_fee_amount=random.uniform(50.0, 500.0),
                shares_investment_funds_discount=random.choice([True, False]),
                shares_investment_funds_discount_amount=random.uniform(10.0, 100.0),
                status=random.choice(['Active', 'Pending', 'Closed'])
            )

            # Create 1-3 Accounts per Product
            for _ in range(random.randint(1, 3)):
                Account.objects.create(
                    client_uuid=client_uuid,
                    product_uuid=product_obj.id,
                    reference_currency=random.choice(['USD', 'EUR', 'GBP', 'CHF', 'JPY']),
                )

        # 10. Create Meeting Preparation
        for _ in range(random.randint(0, 2)):
            MeetingPreparation.objects.create(
                client_uuid=client_uuid,
                place=random.choice(['Internal', 'External']),
                number_of_participants=random.randint(2, 5),
                date_of_meeting=fake.future_date(),
                time=fake.time(),
                hospitality=random.choice(['None', 'Breakfast', 'Lunch']),
                performance_since_beginning=random.uniform(-0.1, 0.2)
            )

        if (i + 1) % 10 == 0:
            print(f"Processed {i + 1} NP clients...")

    # --- Seed Legal Entity (LE) Clients ---
    for i in range(num_le_clients):
        le_client_uuid = uuid.uuid4()
        legal_name = fake.company()

        # 1. LE Hub (Banking Relationship)
        LE_BankingRelationship.objects.create(
            client_uuid=le_client_uuid,
            legal_name=legal_name,
            banking_relationship=f"LE-BR-{random.randint(100000, 999999)}",
            technical_account=random.choice([True, False]),
            additional_br=f"ADD-{random.randint(1000, 9999)}",
            distribution_list=fake.word(),
            name_of_banking_relationship=fake.company(),
            type_of_account=random.choice(['120', '131', '132']),
            type_of_signature=random.choice(['Joint', 'Disjoint']),
            client_segment=random.choice(['Institutional', 'SME', 'Multinational']),
            code_ksc=random.choice(['541', '543', '546', '548', '561', '563', '566', '568']),
            recording_phone_calls=random.choice([True, False]),
            declaration_email=random.choice([True, False]),
            language=random.choice(['German', 'English', 'Spanish']),
            opened_in_ubs_premises=random.choice([True, False]),
            instructions=fake.paragraph(),
            account_and_securities_statements=random.choice([True, False]),
            type_and_purpose=random.choice(['Other',]),
            specify=fake.word(),
            reporting_obligation=random.choice(['Reported by UBS', 'Reported by the client']),
            earning_statement=random.choice([True, False]),
            fees=random.choice([True, False]),
            approval_of_branch_head=random.choice([True, False]),
            fiscal_identifier=fake.bothify(text='FISCAL-#######'),
            agreement_distribution_fees=random.choice([True, False]),
            share_of_distribution=fake.word(),
            send_documents=random.choice([True, False]),
            cscatecosae=fake.bothify(text='CSCATECO-####'),
            further_notes=fake.paragraph(),
            level_of_professionalism=random.randint(1, 5),
            number_of_portfolios=random.randint(1, 10),
            status=random.sample(status_options, k=random.randint(0, 3))
        )

        # 2. LE Company Information
        LE_Company.objects.create(
            client_uuid=le_client_uuid,
            type_of_company=random.choice(['Corporation', 'Partnership', 'Sole Proprietorship', 'LLC']),
            name_of_company=legal_name,
            ivacf=random.choice([True, False]),
            iva=random.choice([True, False]),
            fiscal_code=fake.bothify(text='FC-##########'),
            lei_code=fake.bothify(text='LEI-####################'),
            date_of_constitution=fake.past_date(start_date='-10y'),
            place_of_constitution=fake.city(),
            fiscal_residence=fake.country(),
            turnover_id=fake.bothify(text='TO-########'),
            cciaa_type=random.choice(['Type A', 'Type B', 'Type C']),
            cciaa_number=fake.bothify(text='CCIAA-#######'),
            released_by=fake.name(),
            date_of_issue=fake.past_date(start_date='-5y'),
            form_of_legal_entity=random.choice(['AG', 'GmbH', 'Foundation', 'Trust', 'Other']),
            professional_client_fiduciary_uhnw=random.choice([True, False])
        )

        # 3. LE Personal Information
        LE_PersonalInformation.objects.create(
            client_uuid=le_client_uuid,
            legal_name=legal_name,
            legal_form=random.choice(['AG', 'GmbH', 'Foundation', 'Trust', 'Other']),
            registration_number=fake.bothify(text='REG-#######'),
            country_of_registration=fake.country(),
            date_of_registration=fake.past_date(start_date='-10y'),
            tax_id=fake.bothify(text='VAT-#########'),
            lei_code=fake.bothify(text='LEI-####################'),
            industry_sector=fake.bs(),
            website=fake.url(),
            # Personal Information Fields
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            first_and_last_name=fake.name(),
            name_at_birth=fake.name(),
            federal_state=fake.state(),
            date_of_birth=fake.date_of_birth(minimum_age=25, maximum_age=75),
            place_of_birth=fake.city(),
            country_of_birth=fake.country(),
            marital_status=random.choice(['Single', 'Married', 'Divorced', 'Widowed']),
            occupation_sector=fake.job(),
            fiscal_identifier=fake.bothify(text='FISCAL-#######'),
            indication_tin=random.choice(['Yes', 'No']),
            sensitive_client=random.choice([True, False]),
            executor=random.choice([True, False]),
            beneficial_owner=random.choice([True, False]),
            tef=random.choice([True, False])
        )

        # 4. LE Addresses
        for _ in range(random.randint(1, 3)):
            LE_Address.objects.create(
                client_uuid=le_client_uuid,
                person_entity=fake.name(),
                type_of_address=random.choice(['Domicile', 'Correspondence', 'Third party', 'Tax domicile', 'Fiscal residence']),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                c_o=fake.word(),
                street=fake.street_address(),
                no=fake.building_number(),
                postal_code=fake.zipcode(),
                city=fake.city(),
                province=fake.state(),
                country=fake.country(),
                documents_sent=random.choice([True, False])
            )

        # 5. LE Communications
        for _ in range(random.randint(1, 4)):
            LE_Communication.objects.create(
                client_uuid=le_client_uuid,
                first_and_last_name=fake.name(),
                landline=fake.phone_number(),
                phone=random.choice(['Work', 'Private']),
                phone_number=fake.phone_number(),
                mobile_work=random.choice(['Work', 'Private']),
                mobile_number=fake.phone_number(),
                email=random.choice(['Work', 'Private']),
                email_address=fake.email(),
                fax=random.choice(['Work', 'Private']),
                fax_address=fake.phone_number(),
                pec_address=fake.email()
            )

        # 6. LE Client Advisor
        LE_ClientAdvisor.objects.create(
            client_uuid=le_client_uuid,
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            first_and_last_name=fake.name(),
            email=fake.company_email(),
            desk=fake.word(),
            branch=fake.city(),
            role=random.choice(['Requestor', 'Client Advisor', 'Deputy Client Advisor'])
        )

        # 7. LE Nationalities
        for _ in range(random.randint(1, 2)):
            LE_Nationality.objects.create(
                client_uuid=le_client_uuid,
                is_main_nationality=(_ == 0),
                nationality=fake.country(),
                nci=fake.bothify(text='NCI-########'),
                id_type=random.choice(['Passport', 'ID Card', 'Driver License']),
                fiscal_code=fake.bothify(text='FC-########'),
                fiscal_code_path=f"/path/to/fiscal/{fake.word()}.pdf",
                release_authority=fake.word(),
                release_location=fake.city(),
                release_date=fake.past_date(start_date='-5y'),
                expiry_date=fake.future_date(end_date="+5y"),
                is_id_document_provided=random.choice([True, False]),
                id_document_path=f"/path/to/id/{fake.word()}.pdf"
            )

        # 8. LE TIN, EBanking
        LE_TIN.objects.create(client_uuid=le_client_uuid, aei_tin=fake.bothify(text='TIN-#########'))
        LE_EBanking.objects.create(client_uuid=le_client_uuid, has_ebanking=random.choice([True, False]), contract_number=fake.bothify(text='EB-########'))

        # 9. LE Products and Accounts
        for _ in range(random.randint(1, 3)):
            product_obj = LE_Product.objects.create(
                client_uuid=le_client_uuid,
                portfolio_id=fake.bothify(text='PORT-####'),
                portfolio_name=fake.company() + " Portfolio",
                email_waiver=random.choice([True, False]),
                reference_currency=random.choice(['USD', 'EUR', 'GBP', 'CHF']),
                investment_service=random.choice(['Asset Management', 'Wealth Management', 'Advisory']),
                a_s_authorization_path=f"/path/to/auth/{fake.word()}.pdf",
                investment_strategy=random.choice(['Conservative', 'Balanced', 'Growth', 'Aggressive']),
                ip_risk_tolerance=random.choice(['Low', 'Medium', 'High']),
                investment_amount=random.uniform(10000.0, 1000000.0),
                selected_service=random.choice(['Basic', 'Premium', 'Elite']),
                all_in=random.choice([True, False]),
                sustainable_investing=random.choice([True, False]),
                sustainability_preference=random.choice(['Environmental', 'Social', 'Governance']),
                focus_equity=random.choice([True, False]),
                alternative_investment=random.choice([True, False]),
                direct_instrument=random.choice([True, False]),
                initial_amount=random.uniform(5000.0, 500000.0),
                foreign_hedging=random.choice(['Discretion of UBS', 'None for share allocation']),
                transaction_confirmation=random.choice([True, False]),
                empty_kyc_form_path=f"/path/to/kyc/{fake.word()}.pdf",
                investor_profile_path=f"/path/to/profile/{fake.word()}.pdf",
                myway_module_path=f"/path/to/myway/{fake.word()}.pdf",
                ntac=random.choice(['Excluded', 'Permitted']),
                reporting_loss=random.choice(['Monthly', 'Quarterly']),
                share_focus=random.choice(['EMU: Predominantly...', 'Global equity...']),
                date_of_alignment=fake.date_between(start_date='-1y', end_date='today'),
                end_date_alignment=fake.date_between(start_date='today', end_date='+1y'),
                type_of_business_settlement=random.choice(['Monthly', 'Individual']),
                special_conditions=fake.paragraph(),
                discount_applied=random.choice([True, False]),
                discount_amount_percent=random.uniform(0.0, 50.0),
                flat_fee_applied=random.choice([True, False]),
                flat_fee_percent=random.uniform(0.1, 2.0),
                invested_assets=random.uniform(100000.0, 5000000.0),
                income_pa=random.uniform(1000.0, 50000.0),
                current_return_on_assets=random.uniform(0.01, 0.10),
                target_roa=random.uniform(0.05, 0.15),
                net_new_money_potential=random.uniform(0.0, 1000000.0),
                business_case_communication=random.choice(['Option 1 (in person)', 'Option 2 (online)']),
                fee_model='Advice plus transaction fee',
                mandate_fee=random.choice([True, False]),
                service_and_execution=random.choice(['UBS Manage', 'UBS Advice']),
                no_discount=random.choice([True, False]),
                no_discount_amount_percent=random.uniform(0.0, 10.0),
                no_flat_fee=random.choice([True, False]),
                no_flat_fee_amount=random.uniform(100.0, 1000.0),
                transaction_fee=random.uniform(10.0, 100.0),
                standard_fee_discount=random.uniform(0.0, 20.0),
                shares_fee=random.choice([True, False]),
                shares_fee_amount=random.uniform(50.0, 500.0),
                shares_discount=random.choice([True, False]),
                shares_discount_amount=random.uniform(10.0, 100.0),
                investment_funds_fee=random.choice([True, False]),
                investment_fund_fee_amount=random.uniform(50.0, 500.0),
                investment_fund_discount=random.choice([True, False]),
                investment_fund_discount_amount=random.uniform(10.0, 100.0),
                fixed_income_fee=random.choice([True, False]),
                fixed_income_fee_amount=random.uniform(50.0, 500.0),
                fixed_income_discount=random.choice([True, False]),
                fixed_income_discount_amount=random.uniform(10.0, 100.0),
                fixed_income_investment_funds_fee=random.choice([True, False]),
                fixed_income_investment_funds_fee_amount=random.uniform(50.0, 500.0),
                fixed_income_investment_funds_discount=random.choice([True, False]),
                fixed_income_investment_funds_discount_amount=random.uniform(10.0, 100.0),
                shares_investment_funds_fee=random.choice([True, False]),
                shares_investment_funds_fee_amount=random.uniform(50.0, 500.0),
                shares_investment_funds_discount=random.choice([True, False]),
                shares_investment_funds_discount_amount=random.uniform(10.0, 100.0),
                status=random.choice(['Active', 'Pending', 'Closed'])
            )

            # Create 1-2 Accounts per Product
            for _ in range(random.randint(1, 2)):
                LE_Account.objects.create(
                    client_uuid=le_client_uuid,
                    product_uuid=product_obj.id,
                    reference_currency=random.choice(['USD', 'EUR', 'GBP', 'CHF', 'JPY']),
                )

        # 10. LE Meeting Preparation
        for _ in range(random.randint(0, 2)):
            LE_MeetingPreparation.objects.create(
                client_uuid=le_client_uuid,
                place=random.choice(['Internal', 'External']),
                number_of_participants=random.randint(2, 5),
                date_of_meeting=fake.future_date(),
                time=fake.time(),
                room_booking=random.choice([True, False]),
                hospitality=random.choice(['None', 'Cold drinks, coffee or tea on request', 'Breakfast', 'Lunch']),
                technical_equipment_needed=random.choice([True, False]),
                performance_since_beginning=random.uniform(-0.1, 0.2),
                performance_before_tax=random.uniform(-0.05, 0.15),
                performance_since_start=random.uniform(-0.08, 0.18),
                investor_profile_link=fake.url(),
                email_waiver=random.choice([True, False])
            )

        if (i + 1) % 5 == 0:
            print(f"Processed {i + 1} LE clients...")

    # 11. Create Relationships (Edge Table) - NP and LE
    print("Creating relationships...")
    
    # NP Relationships
    for client_uuid in all_client_uuids:
        # Create 1-3 relationships per client
        for _ in range(random.randint(1, 3)):
            # Pick another client as the target (child_unique_id)
            target_uuid = random.choice(all_client_uuids)
            if target_uuid != client_uuid:
                Relationship.objects.create(
                    client_uuid=client_uuid,
                    child_unique_id=target_uuid,
                    type_of_relationship=random.choice(['POA', 'Joint Owner', 'Family Member', 'Beneficiary']),
                    type_of_access=random.choice(['Full', 'Read-only', 'Limited']),
                    level_of_access=random.sample([
                        'Limited Power of attorney',
                        'Power of attorney for all accounts',
                        'Power of attorney in the event of death'
                    ], k=random.randint(1, 2)),
                    relation_with_owner=random.choice(['Spouse', 'Child', 'Business Partner', 'Legal Rep'])
                )
    
    # LE Relationships
    le_uuids = [le.client_uuid for le in LE_BankingRelationship.objects.all()]
    for le_client_uuid in le_uuids:
        # Create 1-2 relationships per LE client
        for _ in range(random.randint(1, 2)):
            target_uuid = random.choice(le_uuids)
            if target_uuid != le_client_uuid:
                LE_Relationship.objects.create(
                    client_uuid=le_client_uuid,
                    child_unique_id=target_uuid,
                    type_of_relationship=random.choice(['Shareholder', 'Board Member', 'Signatory', 'Beneficiary']),
                    type_of_access=random.choice(['Full', 'Read-only', 'Limited']),
                    level_of_access=random.sample([
                        'Signatory rights',
                        'Board representation',
                        'Voting rights'
                    ], k=random.randint(1, 2)),
                    relation_with_owner=random.choice(['Director', 'Shareholder', 'Legal Representative', 'Authorized Signatory'])
                )

    print(f"Successfully seeded {num_clients} NP and {num_le_clients} LE banking relationships with thousands of related records.")

if __name__ == "__main__":
    count = 20
    if len(sys.argv) > 1:
        try:
            count = int(sys.argv[1])
        except ValueError:
            pass
    bulk_seed(count)
