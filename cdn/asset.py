from postDB import Model, Column, types

from typing import Optional

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
