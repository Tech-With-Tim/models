from postDB import Model, Column, types
from datetime import datetime

import utils


class Challenge(Model):
    """
    Challenge class to store the challenge details made by specific authors
    Database Attributes:
        Attributes stored in the `challenge` table.
        :param int id:              The challenge ID
        :param str title:           The challenge title.
        :param int author_id:       The challenge author's Discord ID.
        :param str description:     The challenge description.
    """

    id = Column(types.Integer(big=True), primary_key=True)
    title = Column(types.String)
    author_id = Column(
        types.ForeignKey("users", "id", sql_type=types.Integer(big=True)),
    )
    description = Column(types.String)
    released_at = Column(types.DateTime, nullable=True)

    @property
    def created_at(self) -> datetime:
        """Returns the time the challenge was created"""
        return utils.snowflake_time(self.id)
