import utils

from datetime import datetime
from postDB import Model, types, Column


class ChallengeSubmission(Model):
    """
    Challenge Submission class

    Database Attributes:
        Attributes stored in the `challengeSubmissions` table.

        :param int id:                   ID of submission
        :param int challenge_id:         The challenge id
        :param int author_id:            ID of submission author
        :param int language_id:          ID of language used in the submission
        :param str code:                 Code submitted
    """

    id = Column(types.Integer(big=True), primary_key=True)
    challenge_id = Column(
        types.ForeignKey("challenges", "id", sql_type=types.Integer(big=True))
    )
    author_id = Column(
        types.ForeignKey("users", "id", sql_type=types.Integer(big=True))
    )
    language_id = Column(
        types.ForeignKey("challengeLanguages", "id", sql_type=types.Integer(big=True))
    )
    code = Column(types.String)

    @property
    def created_at(self) -> datetime:
        """Returns the time the submission was created"""
        return utils.snowflake_time(self.id)
