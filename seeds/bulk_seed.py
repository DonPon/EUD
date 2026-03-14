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
from apps.clients.models import Client, Nationality, Address, Communication, Portfolio, Account

fake = Faker()

def bulk_seed(num_clients=100):
    print(f"Starting bulk seed of {num_clients} clients...")
    
    # 1. Ensure Admin exists
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123', role='ADMIN')
        print("Superuser 'admin' created (pass: admin123)")

    # 2. Clear existing data for a clean test environment (optional, but recommended for testing)
    # Client.objects.all().delete() 

    for i in range(num_clients):
        client_id = uuid.uuid4()
        
        # Create Client
        client = Client.objects.create(
            id=client_id,
            client_uuid=client_id,
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            br_number=f"BR-{random.randint(100000, 999999)}",
            date_of_birth=fake.date_of_birth(minimum_age=18, maximum_age=90),
            status=random.choice(['active', 'active', 'active', 'inactive', 'frozen'])
        )

        # Create 1-2 Nationalities
        for _ in range(random.randint(1, 2)):
            Nationality.objects.create(
                client_uuid=client_id,
                country=fake.country(),
                is_main=(_ == 0) # First one is main
            )

        # Create 1-2 Addresses
        for _ in range(random.randint(1, 3)):
            Address.objects.create(
                client_uuid=client_id,
                street=fake.street_address(),
                city=fake.city(),
                zip_code=fake.zipcode(),
                country=fake.country(),
                is_main=(_ == 0),
                is_domicile=random.choice([True, False]),
                is_tax_domicile=random.choice([True, False]),
                tin=f"TIN-{random.randint(1000, 9999)}"
            )

        # Create 1-3 Communications
        for _ in range(random.randint(1, 6)):
            comm_type = random.choice(['EMAIL', 'PHONE'])
            val = fake.email() if comm_type == 'EMAIL' else fake.phone_number()
            Communication.objects.create(
                client_uuid=client_id,
                comm_type=comm_type,
                value=val,
                is_main=(_ == 0)
            )

        # Create 1-2 Portfolios
        for _ in range(random.randint(1, 10)):
            portfolio_id = uuid.uuid4()
            Portfolio.objects.create(
                id=portfolio_id,
                client_uuid=client_id,
                portfolio_number=f"P-{random.randint(1000, 9999)}-{random.choice(['X', 'Y', 'Z'])}",
                name=f"{fake.word().capitalize()} Portfolio"
            )

            # Create 1-4 Accounts per Portfolio
            for _ in range(random.randint(1, 15)):
                Account.objects.create(
                    client_uuid=client_id,
                    portfolio_uuid=portfolio_id,
                    account_number=fake.iban(),
                    currency=random.choice(['USD', 'EUR', 'GBP', 'CHF', 'JPY']),
                    balance=random.uniform(100.0, 1000000.0)
                )

        if (i + 1) % 10 == 0:
            print(f"Processed {i + 1} clients...")

    print(f"Successfully seeded {num_clients} clients and thousands of related records.")

if __name__ == "__main__":
    import sys
    count = 100
    if len(sys.argv) > 1:
        try:
            count = int(sys.argv[1])
        except ValueError:
            pass
    bulk_seed(count)
