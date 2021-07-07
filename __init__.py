from typing import Type, List
from postDB import Model

from users.user import User
from users.token import Token


models_ordered: List[Type[Model]] = [User, Token]
