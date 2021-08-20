import utils

from typing import Optional, Union
from postDB import types, Model, Column

from ..permissions.bases import BasePermission
from ..permissions.general import Administrator


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
    position = Column(types.Integer, unique=True)
    color = Column(types.Integer, default=0x000000)
    permissions = Column(types.Integer, default=0)

    def __repr__(self):
        return (
            '<Role id="{0.id}" name="{0.name}" '
            'permissions="{0.permissions}" position="{0.position}">'.format(self)
        )

    @classmethod
    async def fetch(cls, id: Union[str, int]) -> Optional["Role"]:
        """Fetch a role with the given ID."""
        query = """
            SELECT
                id::TEXT,
                name,
                position,
                color,
                permissions
            FROM roles WHERE id = $1;
        """
        role = await cls.pool.fetchrow(query, int(id))

        if role is not None:
            role = cls(**role)

        return role

    @classmethod
    async def create(
        cls,
        name: str,
        permissions: int,
        color: Optional[int] = None,
    ):
        """Create a new Role"""
        query = """
        INSERT INTO roles (id, name, color, permissions, position)
            VALUES (
                create_snowflake(), $1, $2, $3, (SELECT COUNT(*) FROM roles) + 1
            )
            RETURNING *;
        """

        color = color or cls.color.default

        record = await cls.pool.fetchrow(query, name, color, permissions)

        return cls(**record)

    async def update(self, **data):
        """Update Role Data"""
        update_query = ["UPDATE roles r SET"]

        fields = (
            "name",
            "color",
            "permissions",
        )
        new_data = {field: data[field] for field in fields if field in data.keys()}

        if len(new_data) > 0:
            update_query.append(
                ", ".join(
                    "r.%s = $%d" % (key, i) for i, key in enumerate(new_data.keys(), 2)
                )
            )

            update_query.append("WHERE r.id = $1 RETURNING *, id::TEXT")

            query = " ".join(update_query)
            record = await self.pool.fetchrow(
                query,
                int(self.id),
                *new_data.values(),
            )

            if record is None:
                return None

            for field, value in record.items():
                setattr(self, field, value)

        if self.position != (position := int(data.get("position", self.position))):
            query = """SELECT COUNT(*) FROM roles;"""
            result = await self.pool.fetchrow(query)
            count = int(result["count"])

            position_query = """SELECT * FROM move_roles($1, $2::BIGINT);"""

            await self.pool.execute(
                position_query,
                max(0, min(position, count)),
                int(self.id),
            )

            self.position = data["position"]

        return self

    def has_permission(self, permission: BasePermission):
        """Returns `True` if this Role has said `Permission`"""
        return self.permissions & permission.value or Administrator().value

    @property
    def created_at(self):
        return utils.snowflake_time(self.id)
