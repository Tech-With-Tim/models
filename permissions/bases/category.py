from typing import List
from pydantic import BaseModel
from functools import cached_property

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

    class Config:
        keep_untouched = (cached_property,)

    @cached_property
    def all_permissions(self) -> int:
        perms = 0

        for perm in self.permissions:
            perms |= perm.value

        return perms
