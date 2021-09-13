from postDB import Model, Column, types
from datetime import datetime

import utils


class Challenge(Model):
    """
    Challenge class to store the challenge details

    Database Attributes:
        Attributes stored in the `challenges` table.

        :param int id:                          The challenge Snowflake ID.
        :param str title:                       The challenge title.
        :param int author_id:                   The challenge author's Discord ID.
        :param str description:                 A description.
        :param List[str] example_in:            Example input.
        :param List[str] example_out:           Example output.
        :param List[int] language_ids:          The languages you can use to complete this challenge.
        :param :class:`datetime` released_at:   The time this challenge was released at.
        :param bool deleted:                    Whether or not this challenge has been deleted.
        :param str slug:                        The URL slug this challenge relates to.
    """

    id = Column(types.Integer(big=True), primary_key=True)
    title = Column(types.String, unique=True)
    author_id = Column(
        types.ForeignKey("users", "id", sql_type=types.Integer(big=True)),
    )
    description = Column(types.String)
    example_in = Column(types.Array(types.String))
    example_out = Column(types.Array(types.String))

    # Implicit ForeignKey to ChallengeLanguage.id
    language_ids = Column(types.Array(types.Integer(big=True)))
    released_at = Column(types.DateTime, nullable=True)
    deleted = Column(types.Boolean, default=False)
    slug = Column(types.String, unique=True)

    @property
    def created_at(self) -> datetime:
        """Returns the time the challenge was created"""
        return utils.snowflake_time(self.id)
