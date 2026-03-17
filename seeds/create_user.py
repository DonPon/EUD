import os
import django
import getpass
import sys

# Add the project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eud_gui.settings')
django.setup()

from apps.users.models import User

def create_admin_user():
    username = getpass.getuser()
    print(f"Creating/Updating user: {username}")
    
    user, created = User.objects.get_or_create(username=username)
    user.role = User.Role.ADMIN
    user.is_staff = True
    user.is_superuser = True
    user.save()
    
    if created:
        print(f"Successfully created ADMIN user: {username}")
    else:
        print(f"Successfully updated user {username} to ADMIN")

if __name__ == "__main__":
    create_admin_user()
