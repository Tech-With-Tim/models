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
        :param str rules:           The rules of the challenge.
        :param int reward:          The reward for completing the challenge.
    """

    id = Column(types.Integer(big=True), primary_key=True)
    # Store the ID as a BIGINT even though it's transferred as a string.
    # This is due to a substantial difference in index time and storage space
    title = Column(types.String)
    author_id = Column(
        types.ForeignKey("users", "id", sql_type=types.Integer(big=True)),
    )
    description = Column(types.String)
    rules = Column(types.String)
    reward = Column(types.Integer)

    @property
    def created_at(self) -> datetime:
        """Returns the time the challenge was created"""
        return utils.snowflake_time(self.id)
