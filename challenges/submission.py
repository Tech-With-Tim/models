from postDB import Model, Column, types
from datetime import datetime

import utils


class Submission(Model):
    """
    Challenge class to store the challenge details made by specific authors
    Database Attributes:
        Attributes stored in the `challenge` table.
        :param int id:              The submission ID
        :param int challenge_id:    The submission challenge ID.
        :param str code:            The submission code.
        :param str language:        The submission language.
        :param int author_id:       The submission author.
    """

    id = Column(types.Integer(big=True), primary_key=True)
    # Store the ID as a BIGINT even though it's transferred as a string.
    # This is due to a substantial difference in index time and storage space
    challenge_id = Column(
        types.ForeignKey("challenge", "id", sql_type=types.Integer(big=True)),
    )

    code = Column(types.String)
    language = Column(types.String)

    author_id = Column(
        types.ForeignKey("users", "id", sql_type=types.Integer(big=True)),
    )

    def created_at(self) -> datetime:
        """Returns"""
        return utils.snowflake_time(self.id)
