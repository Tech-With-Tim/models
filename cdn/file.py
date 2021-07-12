from postDB import Model, Column, types

from typing import Union, Optional
from datetime import datetime

import utils


class File(Model):
    """
    File class mapped to Asset models..

    Database Attributes:
        Attributes stored in the `files` table.

        :param int id:              The file ID.
        :param str name:            The file name.
        :param str mimetype:        The files mimetype.
        :param bytes data:          The binary data (the file itself)
    """

    id = Column(types.Integer(big=True), unique=True)
    mimetype = Column(types.String)
    name = Column(types.String)
    data = Column(types.Binary)

    @classmethod
    async def fetch(cls, id: Union[str, int]) -> Optional["File"]:
        """Fetch a `File` with the given id."""
        query = "SELECT * FROM files WHERE id = $1"
        record = await cls.pool.fetchrow(query, int(id))

        if record is None:
            return None

        return cls(**record)

    @property
    def created_at(self) -> "datetime":
        """Returns the objects creation time in UTC."""
        return utils.snowflake_time(id=self.id, internal=True)
