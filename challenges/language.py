import utils

from datetime import datetime
from postDB import Model, types, Column


class ChallengeLanguage(Model):
    """
    Challenge Languages class

    Database Attributes:
        Attributes stored in the `challengelanguages` table.

        :param int id:                  Snowflake ID
        :param str name:                Unique language name
        :param str download_url:        Optional download url.
        :param int disabled:            Whether or not this language is disabled.
        :param str piston_lang:         The language this correlates to in piston API.
        :param str piston_lang_ver:     The version of the specified language e.g. python (3.8.10)
    """

    id = Column(types.Integer(big=True), primary_key=True)
    name = Column(types.String, unique=True)
    download_url = Column(types.String, nullable=True)
    disabled = Column(types.Boolean, default=False)
    piston_lang = Column(types.String)
    piston_lang_ver = Column(types.String)

    @property
    def created_at(self) -> datetime:
        """Returns the time the language was created in our db"""
        return utils.snowflake_time(self.id)
