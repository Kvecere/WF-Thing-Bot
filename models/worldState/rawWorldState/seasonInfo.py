from typing import Optional
from models.worldState.rawWorldState.common import DateObject, IdObject


class SeasonActiveChallenge:
    id: IdObject
    daily: Optional[bool]
    activation: DateObject
    expiry: DateObject
    challenge: str

class SeasonInfo:
    """Information about the current Nightwave"""
    activation: DateObject
    expiry: DateObject
    affiliationTag: str
    season: int
    phase: int
    params: str
    activeChallenges: list[SeasonActiveChallenge]