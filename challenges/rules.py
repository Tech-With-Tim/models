from postDB import Model, types, Column


class ChallengeRules(Model, name="ChallengeRules"):
    """
    Challenge Rules class

    Database Attributes:
        Attributes stored in the `challengeRules` table.
        :param int challenge_id:         The challenge id
        :param bool can_use_imports:     Are imports allowed?
    """

    challenge_id = Column(
        types.ForeignKey("challenges", "id", sql_type=types.Integer(big=True))
    )
    can_use_imports = Column(types.Boolean)
    # add other rules later...
