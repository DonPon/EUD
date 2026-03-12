import os
import django
import uuid
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eud_test.settings')
django.setup()

from apps.users.models import User
from apps.clients.models import Client, Nationality, Address, Communication, Portfolio, Account

def seed():
    # 1. Create Superuser
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123', role='ADMIN')
        print("Superuser 'admin' created (pass: admin123)")
    else:
        print("Superuser 'admin' already exists.")

    # 2. Clear existing bank data to avoid conflicts with new schema
    Client.objects.all().delete()

    # 3. Create sample bank client
    client_id = uuid.uuid4()
    client = Client.objects.create(
        id=client_id,
        client_uuid=client_id,
        first_name="Jane",
        last_name="Smith",
        br_number="BR-998877",
        date_of_birth=date(1990, 1, 1),
        status="active"
    )
    print(f"Bank Client created: {client}")

    # 4. Add Nationalities
    Nationality.objects.create(client_uuid=client_id, country="Switzerland", is_main=True)
    Nationality.objects.create(client_uuid=client_id, country="Italy", is_main=False)

    # 5. Add Addresses
    Address.objects.create(
        client_uuid=client_id,
        street="Bahnhofstrasse 1",
        city="Zurich",
        zip_code="8001",
        country="Switzerland",
        is_main=True,
        is_domicile=True,
        is_tax_domicile=True,
        tin="CHE-123.456.789"
    )

    # 6. Add Communications
    Communication.objects.create(client_uuid=client_id, comm_type="EMAIL", value="jane.smith@example.ch", is_main=True)
    Communication.objects.create(client_uuid=client_id, comm_type="PHONE", value="+41 44 123 45 67", is_main=True)

    # 7. Add Portfolio
    portfolio_id = uuid.uuid4()
    portfolio = Portfolio.objects.create(
        id=portfolio_id,
        client_uuid=client_id,
        portfolio_number="P-5500-X",
        name="Main Investment Portfolio"
    )

    # 8. Add Accounts to Portfolio
    Account.objects.create(
        client_uuid=client_id,
        portfolio_uuid=portfolio_id,
        account_number="CH-001-ACC",
        currency="CHF",
        balance=150000.00
    )
    Account.objects.create(
        client_uuid=client_id,
        portfolio_uuid=portfolio_id,
        account_number="US-002-ACC",
        currency="USD",
        balance=50000.00
    )

    print("Bank-centric seed data created successfully.")

if __name__ == "__main__":
    seed()
