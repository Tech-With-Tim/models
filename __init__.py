from postDB import Model
from typing import Type, List

from .cdn import Asset, File
from .users import User, Token
from .roles import Role, UserRole
from .challenges import (
    Challenge,
    ChallengeRules,
    ChallengeRewards,
    ChallengeLanguage,
    ChallengeSubmission,
)


models_ordered: List[Type[Model]] = [
    User,
    Token,
    File,
    Asset,
    Role,
    UserRole,
    Challenge,
    ChallengeRules,
    ChallengeRewards,
    ChallengeLanguage,
    ChallengeSubmission,
]
