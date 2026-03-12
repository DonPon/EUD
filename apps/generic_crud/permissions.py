from rest_framework import permissions

class RoleBasedPermission(permissions.BasePermission):
    """
    Granular RBAC for the Bank system:
    - ADMIN: Full access (CRUD + History).
    - EDITOR: Can View, Create, and Edit (GET, POST, PUT, PATCH). No Delete.
    - VIEWER: Read-only access (GET).
    """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        role = request.user.role

        # Admin has full access
        if role == 'ADMIN':
            return True

        # Editor can do everything except DELETE
        if role == 'EDITOR':
            return request.method not in ['DELETE']

        # Viewer can only do Safe Methods (GET, HEAD, OPTIONS)
        if role == 'VIEWER':
            return request.method in permissions.SAFE_METHODS

        return False

    def has_object_permission(self, request, view, obj):
        # We can add object-level logic here if needed (e.g., data layer permissions)
        return self.has_permission(request, view)
