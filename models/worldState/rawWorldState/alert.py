from typing import Optional
from models.worldState.rawWorldState.common import DateObject, Faction, IdObject, MissionType, Reward

class AlertMissionInfo:
    """Represents an Alert seen in the 'Alerts' tab in the navigation screen."""
    location: str
    missionType: MissionType
    faction: Faction
    difficulty: int
    missionReward: list[Reward]
    levelOverride: str
    enemySpec: str
    extraEnemySpec: Optional[str]
    questReq: Optional[str]
    minEnemyLevel: int
    maxEnemyLevel: int
    descText: Optional[str]
    maxWaveNum: Optional[int]

class Alert:
    id: IdObject
    activation: DateObject
    expiry: DateObject
    missionInfo: AlertMissionInfo
    tag: str
    """Can be Hard or LotusGift"""
    ForceUnlock: Optional[bool]