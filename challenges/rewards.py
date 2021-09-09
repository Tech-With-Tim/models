from postDB import Model, types, Column


class ChallengeRewards(Model, name="ChallengeRewards"):
    """
    Challenge Rewards class

    Database Attributes:
        Attributes stored in the `challengeRewards` table.
        :param int challenge_id:         The challenge id
        :param bool coins:               Coins rewarded to participants
        :param bool tokens:              Challenge tokens rewarded to participants
        :param bool xp:                  Xp rewarded to participants
    """

    challenge_id = Column(
        types.ForeignKey("challenges", "id", sql_type=types.Integer(big=True))
    )
    coins = Column(types.Real)
    tokens = Column(types.Integer)
    xp = Column(types.Integer)
