import utils

from datetime import datetime
from postDB import Model, types, Column


class ChallengeLanguage(Model):
    """
    Challenge Languages class

    Database Attributes:
        Attributes stored in the `challengeLanguages` table.
        :param int id:                  The language ID
        :param str name:                The language name
        :param int download_url:
        :param str piston_runtime:      The runtime used in piston to run the language
        :param int disabled:
    """

    id = Column(types.Integer(big=True))
    name = Column(types.String)
    download_url = Column(types.String)
    piston_runtime = Column(types.String)
    code_template = Column(types.String)
    disabled = Column(types.Boolean, default=False)

    @property
    def created_at(self) -> datetime:
        """Returns the time the language was created in our db"""
        return utils.snowflake_time(self.id)
