import os
import sys
import django
import uuid
import argparse
from pathlib import Path
from django.utils import timezone

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

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eud_gui.settings')
django.setup()

from apps.dashboard_bots.models import Bot, BotStatus, BotRecord

def seed_data():
    print("Starting bot seeding...")
    
    # Define the bots and their metadata
    bots_to_create = [
        ("Bot 0", "Initial Data Ingestion and Validation bot."),
        ("Bot 3", "Portfolio Risk Analysis engine."),
        ("Bot 7_1", "Compliance Screener - AML/KYC Phase 1."),
        ("Bot 7_2", "Compliance Screener - Enhanced Due Diligence Phase 2."),
        ("Bot 8", "Automated Account Reconciliation."),
        ("Bot 11", "Client Reporting and Monthly Statement Generator."),
    ]

    statuses = ["Not Running", "Not Running", "Not Running", "Not Running", "Not Running", "Not Running"]
    
    for i, (name, desc) in enumerate(bots_to_create):
        # 1. Create Bot Configuration
        bot, created = Bot.objects.get_or_create(
            name=name,
            defaults={
                'description': desc,
            }
        )
        if created:
            print(f"Created configuration for {name}")

        # 2. Create/Update Current Bot Status
        status_val = statuses[i % len(statuses)]
        BotStatus.objects.update_or_create(
            bot=name,
            defaults={
                'bot_status': status_val,
            }
        )
        print(f"Set status for {name} to {status_val}")

        # 3. Create Sample Execution Records
        # Create 5 records for each bot with varying statuses
        for j in range(5):
            rec_status = "Success" if (i + j) % 3 != 0 else "Failed"
            msg = "Processed successfully" if rec_status == "Success" else "Network timeout during validation"
            
            BotRecord.objects.create(
                bot_name=name,
                bank_rel=f"BR-{2000 + i}-{j}",
                start_time=timezone.now() - timezone.timedelta(days=j, hours=i),
                end_time=timezone.now() - timezone.timedelta(days=j, hours=i-1),
                status=rec_status,
                message=msg,
                client_type="Individual" if j % 2 == 0 else "Corporate",
                t_number=f"T{8000 + i}",
                run_identifier=f"RUN-{uuid.uuid4().hex[:8].upper()}",
            )
        print(f"Generated 5 sample records for {name}")

    print("\nSeeding complete! You can now view the Dashboard.")

if __name__ == "__main__":
    seed_data()
