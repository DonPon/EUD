import os
import sys
import time
import uuid
import random
import django
from datetime import timedelta
from pathlib import Path

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eud_gui.settings')
django.setup()

from apps.dashboard_bots.models import Bot, BotStatus, BotRecord
from apps.clients.models import BankingRelationship
from apps.clients_le.models import LE_BankingRelationship
from django.utils import timezone

def run_simulation(duration_seconds):
    """
    Simulates bot activity by randomly switching bot statuses and creating execution records.
    """
    print(f"====================================================")
    print(f"Starting Bot Dashboard Simulation")
    print(f"Duration: {duration_seconds} seconds")
    print(f"====================================================")

    bots = list(Bot.objects.all()[:2])
    
    # Load regular clients and LE clients
    regular_clients = list(BankingRelationship.objects.all()[:3])
    le_clients = list(LE_BankingRelationship.objects.all()[:2])
    clients = regular_clients + le_clients

    if not bots:
        print("Error: No bots found in database. Please run 'python seeds/seed_bots.py' first.")
        return
    
    if not clients:
        print("Warning: No clients found in database. Using dummy BR numbers.")
    else:
        print(f"Loaded {len(clients)} clients ({len(regular_clients)} Regular, {len(le_clients)} LE) for case processing simulation.")

    start_time = time.time()
    
    # Initialize bot states
    # Options: Running, Success, Failed, Idle, Paused
    current_states = {}
    next_toggle_time = {}
    
    for bot in bots:
        # Start some as running, some as idle
        initial_status = random.choice(["Running", "Idle", "Success"])
        current_states[bot.name] = initial_status
        next_toggle_time[bot.name] = time.time() + random.uniform(2, 8)
        
        # Update initial status in DB
        BotStatus.objects.update_or_create(
            bot=bot.name,
            defaults={'bot_status': initial_status}
        )

    try:
        while (time.time() - start_time) < duration_seconds:
            now = time.time()
            elapsed = int(now - start_time)
            
            for bot in bots:
                # 1. Check if we should toggle the bot status (approx every 7 seconds)
                if now >= next_toggle_time[bot.name]:
                    old_status = current_states[bot.name]
                    
                    if old_status == "Running":
                        # If running, it either finishes or goes idle
                        new_status = random.choice(["Idle", "Success", "Failed"])
                    else:
                        # If not running, it starts running
                        new_status = "Running"
                    
                    current_states[bot.name] = new_status
                    # Schedule next toggle (4 to 10 seconds range)
                    next_toggle_time[bot.name] = now + random.uniform(4, 10)
                    
                    # Update BotStatus in DB
                    BotStatus.objects.update_or_create(
                        bot=bot.name,
                        defaults={'bot_status': new_status}
                    )
                    
                    status_label = "[RUNNING]" if new_status == "Running" else "[STATUS]"
                    print(f"[{elapsed}s] {status_label} {bot.name}: {old_status} -> {new_status}")

                # 2. If bot is "Running", simulate case processing
                if current_states[bot.name] == "Running":
                    # ~20% chance per second to process a new case
                    if random.random() < 0.2:
                        if clients:
                            target_client = random.choice(clients)
                            br_num = target_client.banking_relationship
                            
                            # Determine client type based on model
                            if isinstance(target_client, LE_BankingRelationship):
                                c_type = "Corporate (LE)"
                            else:
                                # For regular clients, we could use their segment or just random
                                c_type = random.choice(["Individual", "Corporate"])
                        else:
                            br_num = f"BR-{random.randint(100000, 999999)}"
                            c_type = "Simulation"

                        rec_status = random.choice(["Success", "Success", "Success", "Failed"])
                        msg = "Automated processing completed" if rec_status == "Success" else "Connection timeout - retrying later"
                        
                        # Create a new BotRecord
                        BotRecord.objects.create(
                            bot_name=bot.name,
                            bank_rel=br_num,
                            start_time=timezone.now() - timedelta(seconds=random.randint(2, 10)),
                            end_time=timezone.now(),
                            status=rec_status,
                            message=msg,
                            client_type=c_type,
                            t_number=f"T{random.randint(8000, 8999)}",
                            run_identifier=f"RUN-{uuid.uuid4().hex[:8].upper()}"
                        )
                        print(f"[{elapsed}s] {bot.name} processed case for {br_num} ({rec_status})")

            time.sleep(1)

    except KeyboardInterrupt:
        print("\n\nSimulation interrupted by user.")
    
    print(f"\n====================================================")
    print(f"Simulation finished after {int(time.time() - start_time)} seconds.")
    print(f"====================================================")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Run a real-time simulation of bot activity.")
    parser.add_argument("seconds", type=int, nargs="?", default=60, help="Duration in seconds (default: 60)")
    
    args = parser.parse_args()
    
    run_simulation(args.seconds)
