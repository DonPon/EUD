"""
Script will create the user account, 20 test cases for NP and LE and also the BOTS table with some test rata runs.
"""

import sys
import argparse

# Parse config-file argument if present and pass it to imported scripts
parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("--config-file", type=str, default="")
args, remaining = parser.parse_known_args()

# Store config file path in environment variable for settings.py to use
if args.config_file:
    import os
    os.environ["EUD_CONFIG_FILE"] = args.config_file

from bulk_seed import bulk_seed
from create_user import create_admin_user
from seed_bots import seed_data


create_admin_user()
bulk_seed(20)
seed_data()