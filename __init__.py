from typing import Type, List
from postDB import Model

from .cdn import Asset, File
from .users import User, Token
from .challenges import Challenge, ChallengeSubmission


models_ordered: List[Type[Model]] = [
    User,
    Token,
    File,
    Asset,
    Challenge,
    ChallengeSubmission,
]
