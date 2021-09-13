from typing import List
from .bases import BasePermission, BaseCategory


class CreateWeeklyChallenge(BasePermission):
    """A permission which allows users to create new weekly challenges"""

    id: int = 3
    name: str = "Create Challenge"
    value: int = 1 << 2
    description: str = "Allows users to create new weekly challenges"


class EditWeeklyChallenge(BasePermission):
    """A permission which allows users to edit weekly challenges created by anyone"""

    id: int = 4
    name: str = "Edit Challenges"
    value: int = 1 << 3
    description: str = "Allows users to edit weekly challenges"


class ViewUpcomingWeeklyChallenge(BasePermission):
    """A permission which allows users to view upcoming (not published) weekly challenges"""

    id: int = 5
    name: str = "View Upcoming Challenges"
    value: int = 1 << 4
    description: str = "Allows users to view upcoming (not published) weekly challenges"


class DeleteWeeklyChallenge(BasePermission):
    """A permission which allows users to delete weekly challenges"""

    id: int = 6
    name: str = "Delete Challenge"
    value: int = 1 << 5
    description: str = "Allows users to delete weekly challenges"


class ManageParticipants(BasePermission):
    """A permission which allows users to manage weekly challenges participants"""

    id: int = 7
    name: str = "Manage Participants"
    value: int = 1 << 6
    description: str = "Allows users to remove or ban weekly challenges participants"


class ManageSubmissions(BasePermission):
    """A permission which allows users to manage weekly challenges submissions"""

    id: int = 8
    name: str = "Manage Submissions"
    value: int = 1 << 7
    description: str = "Allows users to manage weekly challenges submissions"


class ManageWeeklyChallengeLanguages(BasePermission):
    """A permission which allows users to manage weekly challenge languages"""

    id: int = 9
    name: str = "Manage Weekly Challenge Languages"
    value: int = 1 << 8
    description: str = "Allows users to manage weekly challenge languages"


class WeeklyChallengesPermissions(BaseCategory):
    """Weekly Challenges Related Permissions"""

    name: str = "Weekly Challenges"

    permissions: List[BasePermission] = [
        CreateWeeklyChallenge(),
        EditWeeklyChallenge(),
        ViewUpcomingWeeklyChallenge(),
        DeleteWeeklyChallenge(),
        ManageParticipants(),
        ManageSubmissions(),
        ManageWeeklyChallengeLanguages(),
    ]
