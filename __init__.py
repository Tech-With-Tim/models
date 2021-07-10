from typing import Type, List
from postDB import Model

from .users import User, Token
from .challenges import Challenge, ChallengeSubmission
from .cdn import Asset, File


models_ordered: List[Type[Model]] = [
    Asset,
    File,
    User,
    Token,
    Challenge,
    ChallengeSubmission,
]
