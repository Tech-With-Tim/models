from postDB import Model, Column, types

from typing import Optional
from datetime import datetime

import utils

from .file import File


class Asset(Model):
    """
    Asset class used in the CDN and Badge class.

    Database Attributes:
        Attributes stored in the `assets` table.

        :param int id:              The asset ID.
        :param str name:            The asset name to be displayed on web-dashboard.
        :param str url_path:        The CDN path this Asset should be mapped to
        :param int file_id:         The file this Asset maps to.
    """

    id = Column(types.Integer(big=True), unique=True)
    name = Column(types.String(length=64))
    url_path = Column(types.String, primary_key=True)
    file_id = Column(types.ForeignKey("files", "id", sql_type=types.Integer(big=True)))
    creator_id = Column(
        types.ForeignKey("users", "id", sql_type=types.Integer(big=True))
    )

    file: Optional["File"] = None

    @classmethod
    async def fetch(cls, **kwargs) -> Optional["Asset"]:
        """
        Fetch Asset based on any of the provided arguments.
        If `None` is given it will not be acquainted for in the query.

        :param int id:          Asset ID
        :param str name:        Asset name
        :param str url_path:    Asset url path
        :return:                Optional[Asset]
        """
        args = []
        query = "SELECT * FROM {}".format(cls.__tablename__)

        for key in ("id", "name", "url_path"):
            value = kwargs.get(key)
            if value is None:
                continue

            if key == "id" and isinstance(value, str):
                value = int(value)

            query += f" {'WHERE' if not args else 'AND'} {key} = ${len(args)+1}"
            args.append(value)

        record = await cls.pool.fetchrow(query, *args)
        if record is None:
            return None

        return cls(**record)

    @property
    def created_at(self) -> "datetime":
        """Returns the objects creation time in UTC."""
        return utils.snowflake_time(id=self.id, internal=True)
