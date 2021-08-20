from typing import List
from pydantic import BaseModel

from .permission import BasePermission


class BaseCategory(BaseModel):
    """
    Base class for a permission category

    Attributes:
        :param str name:                The name of the permission category
        :param List[BasePermission]:    A list of the permissions this category has
    """

    name: str
    permissions: List[BasePermission]

    @property
    def all_permissions(self) -> int:
        perms = 0

        for perm in self.permissions:
            perms |= perm.value

        return perms