import getpass
from django.contrib.auth import login, get_user_model
from django.utils.deprecation import MiddlewareMixin

User = get_user_model()

class DevSSOMiddleware(MiddlewareMixin):
    """
    Middleware to automatically login the user based on the OS username.
    This is intended for local development ONLY.
    """
    def process_request(self, request):
        # Only attempt to auto-login if the user is not already authenticated
        if not request.user.is_authenticated:
            username = getpass.getuser()
            try:
                # Find the user by OS username
                user = User.objects.get(username=username)
                
                # In a real SSO, you might want to authenticate through a backend.
                # Here, we specify the backend to use for logging in.
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                
                # Automatically login the user for this session
                login(request, user)
                print(f"DEBUG: Auto-logged in user: {username} with role: {user.role}")
            except User.DoesNotExist:
                # If the user doesn't exist, we don't auto-login
                print(f"DEBUG: User '{username}' not found in DB. Skipping auto-login.")
                pass
