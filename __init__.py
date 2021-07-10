from typing import Type, List
from postDB import Model

from .users.user import User
from .users.token import Token
from .challenges.challenge import Challenge
from .challenges.challenge_submission import ChallengeSubmission
from .cdn import Asset, File


models_ordered: List[Type[Model]] = [
    User,
    Token,
    Challenge,
    ChallengeSubmission,
    Asset,
    File,
]
