import utils

from typing import List, Optional, Union
from postDB import types, Model, Column

from ..permissions import Administrator
from ..permissions.bases import BasePermission


class Role(Model):
    """
    Role class

    Database Attributes:
        Attributes stored in the `roles` table.
        :param int id:                          Role ID.
        :param str name:                        Role name.
        :param int color:                       The color this role is.
        :param int position:                    The position this role is in the hierarchy.
        :param int permissions:                 The permissions this role has.
    """

    id = Column(types.Integer(big=True), primary_key=True)
    name = Column(types.String(length=32))
    position = Column(types.Numeric)
    color = Column(types.Integer, nullable=True)
    permissions = Column(types.Integer, default=0)

    def __repr__(self):
        return (
            "<Role id={0.id!r} name={0.name!r} "
            "permissions={0.permissions!r} position={0.position!r}>".format(self)
        )

    @classmethod
    async def fetch(cls, id: Union[str, int]) -> Optional["Role"]:
        """Fetch a role with the given ID."""
        query = """SELECT * FROM roles WHERE id = $1;"""
        role = await cls.pool.fetchrow(query, int(id))

        if role is not None:
            role = cls(**role)

        return role

    def has_permissions(self, permissions: List[Union[int, BasePermission]]) -> bool:
        """Returns `True` if this Role has all `Permissions`"""
        if self.permissions & Administrator().value:
            return True

        all_perms = 0
        for perm in permissions:
            if isinstance(perm, int):
                all_perms |= perm
            else:
                all_perms |= perm.value

        return self.permissions & all_perms == all_perms

    def has_permission(self, permission: Union[BasePermission, int]) -> bool:
        """Returns `True` if this Role has said `Permission`"""
        if self.permissions & Administrator().value:
            return True

        if isinstance(permission, int):
            return self.permissions & permission == permission

        return self.permissions & permission.value == permission.value

    @property
    def created_at(self):
        return utils.snowflake_time(self.id)
