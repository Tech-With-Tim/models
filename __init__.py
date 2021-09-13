from postDB import Model
from typing import Type, List

from .cdn import Asset, File
from .users import User, Token
from .roles import Role, UserRole
from .challenges import (
    Challenge,
    ChallengeLanguage,
    ChallengeSubmission,
    ChallengeParticipant,
)


models_ordered: List[Type[Model]] = [
    User,
    Token,
    File,
    Asset,
    Role,
    UserRole,
    ChallengeLanguage,
    Challenge,
    ChallengeSubmission,
    ChallengeParticipant,
]
