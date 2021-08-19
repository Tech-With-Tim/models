from pydantic import BaseModel


class BasePermission(BaseModel):
    """
    Base class for a permission

    Attributes:
        :param str id:             The id of the permission
        :param str name:           The name of the permission
        :param str value:          The value of the permission
        :param str description:    Description of what the permission allows
    """

    id: int
    name: str
    value: int
    description: str
