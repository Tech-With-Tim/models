from .bases import BasePermission, BaseCategory
from .general import GeneralPermissions, Administrator, ManageRoles
from .challenges import (
    WeeklyChallengesPermissions,
    CreateWeeklyChallenge,
    DeleteWeeklyChallenge,
    EditWeeklyChallenge,
    ManageParticipants,
    ManageSubmissions,
    ManageWeeklyChallengeLanguages,
    ViewUpcomingWeeklyChallenge,
)


__all__ = (
    BasePermission,
    BaseCategory,
    Administrator,
    ManageRoles,
    GeneralPermissions,
    WeeklyChallengesPermissions,
    CreateWeeklyChallenge,
    DeleteWeeklyChallenge,
    EditWeeklyChallenge,
    ManageParticipants,
    ManageSubmissions,
    ManageWeeklyChallengeLanguages,
    ViewUpcomingWeeklyChallenge,
)
