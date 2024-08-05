from typing import Optional

from models.worldState.rawWorldState.common import DateObject, FissureType, IdObject, MissionType, Region


class ActiveMission:
    """Represents a fissure"""
    id: IdObject
    region: Region
    seed: int
    activation: DateObject
    expiry: DateObject
    node: str
    missionType: MissionType
    modifier: FissureType
    hard: Optional[bool]
    """Whether or not it's a steel path fissure"""