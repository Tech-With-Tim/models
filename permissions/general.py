from typing import List

from .bases import BaseCategory, BasePermission


class Administrator(BasePermission):
    """Administrator permission gives every permission"""

    id = 1
    name = "Administrator"
    value = 1 << 0
    description = "Users with this permission will have every permission"


class ManageRoles(BasePermission):
    """Manage roles permission allows management and editing of roles."""

    id = 2
    name = "Manage Roles"
    value = 1 << 1
    description = "Users with this permission will be able to manage and edit roles lower than their highest role"


class GeneralPermissions(BaseCategory):
    """General Permissions"""

    name: str = "General Permissions"
    permissions: List[BasePermission] = [
        Administrator(),
        ManageRoles(),
    ]
