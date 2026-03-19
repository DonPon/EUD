"""
Script will create the user account, 20 test cases for NP and LE and also the BOTS table with some test rata runs.
"""

from bulk_seed import bulk_seed
from create_user import create_admin_user
from seed_bots import seed_data


create_admin_user()
bulk_seed(20)
seed_data()