import os
import sys
import django
import uuid
import random
from datetime import date, timedelta
from pathlib import Path
from faker import Faker

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
    LE_BankingRelationship, LE_Information, LE_Address, LE_Communication
)

fake = Faker()

def bulk_seed(num_clients=20, num_le_clients=10):
    print(f"Starting bulk seed of {num_clients} NP and {num_le_clients} LE banking relationships...")

    status_options = ['review_needed', 'ready_for_bot_1', 'ready_for_bot_2', 'ready_for_bot_3','ready_for_bot_4', 'ready_for_bot_5', 'ready_for_bot_6', 'ready_for_bot_7', 'ready_for_bot_8', 'completed']

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
                product_name=random.choice(['Savings Account', 'Credit Card', 'Mortgage', 'Investment Fund', 'Portfolio']),
                product_id=fake.bothify(text='PROD-####'),
                status=random.choice(['Active', 'Pending', 'Closed'])
            )

            # Create 1-3 Accounts per Product
            for _ in range(random.randint(1, 3)):
                Account.objects.create(
                    client_uuid=client_uuid,
                    product_uuid=product_obj.id,
                    account_number=fake.iban(),
                    currency=random.choice(['USD', 'EUR', 'GBP', 'CHF', 'JPY']),
                    balance=random.uniform(1000.0, 500000.0)
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
        
        # 1. LE Hub
        LE_BankingRelationship.objects.create(
            client_uuid=le_client_uuid,
            legal_name=legal_name,
            banking_relationship=f"LE-BR-{random.randint(100000, 999999)}",
            technical_account=random.choice([True, False]),
            client_segment=random.choice(['Institutional', 'SME', 'Multinational']),
            code_ksc=random.choice(['541', '561']),
            language=random.choice(['English', 'German']),
            status=random.sample(status_options, k=random.randint(0, 2))
        )

        # 2. LE Information
        LE_Information.objects.create(
            client_uuid=le_client_uuid,
            legal_name=legal_name,
            legal_form=random.choice(['AG', 'GmbH', 'Foundation', 'Trust']),
            registration_number=fake.bothify(text='REG-#######'),
            country_of_registration=fake.country(),
            date_of_registration=fake.past_date(),
            tax_id=fake.bothify(text='VAT-#########'),
            lei_code=fake.bothify(text='LEI-####################'),
            industry_sector=fake.bs(),
            website=fake.url()
        )

        # 3. LE Addresses
        for addr_type in ['Registered Office', 'Business Address']:
            LE_Address.objects.create(
                client_uuid=le_client_uuid,
                type_of_address=addr_type,
                street=fake.street_address(),
                no=fake.building_number(),
                postal_code=fake.zipcode(),
                city=fake.city(),
                country=fake.country()
            )

        # 4. LE Communications
        for dept in ['Finance', 'Legal', 'Operations']:
            LE_Communication.objects.create(
                client_uuid=le_client_uuid,
                department=dept,
                contact_person=fake.name(),
                phone_number=fake.phone_number(),
                email_address=fake.company_email()
            )

        if (i + 1) % 5 == 0:
            print(f"Processed {i + 1} LE clients...")

    # 11. Create Relationships (Edge Table)
    print("Creating relationships...")
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

    print(f"Successfully seeded {num_clients} relationships and thousands of related records.")

if __name__ == "__main__":
    count = 20
    if len(sys.argv) > 1:
        try:
            count = int(sys.argv[1])
        except ValueError:
            pass
    bulk_seed(count)
