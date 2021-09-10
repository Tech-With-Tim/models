from postDB import Model, Column, types
from datetime import datetime

import utils


class ChallengeParticipant(Model):
    """
    ChallengeParticipant class to store users that viewed challenges.

    Database Attributes:
        Attributes stored in the `challengeparticipants` table.

        :param int id:              Snowflake ID.
        :param int challenge_id:    The challenge they viewed.
        :param int user_id:         The user ID.
    """

    id = Column(types.Integer(big=True), primary_key=True)
    challenge_id = Column(
        types.ForeignKey("challenges", "id", sql_type=types.Integer(big=True))
    )
    user_id = Column(types.ForeignKey("users", "id", sql_type=types.Integer(big=True)))

    @property
    def created_at(self) -> datetime:
        """Returns the time the user viewed this challenge."""
        return utils.snowflake_time(self.id)
