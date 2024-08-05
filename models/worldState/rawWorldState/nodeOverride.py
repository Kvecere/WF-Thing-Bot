from typing import Optional
from models.worldState.rawWorldState.common import DateObject, Faction, IdObject


class NodeOverride:
    id: IdObject
    node: str
    hide: Optional[bool]
    seed: Optional[int]
    levelOverride: Optional[str]
    activation: Optional[DateObject]
    expiry: Optional[DateObject]
    faction: Optional[Faction]
    enemySpec: str
    extraEnemySpec: str
    customNpcEncounters: Optional[list[str]]