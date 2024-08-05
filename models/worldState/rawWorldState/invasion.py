from typing import Optional
from models.worldState.rawWorldState.common import DateObject, Faction, IdObject, Reward


class InvasionMissionInfo:
    seed: int
    faction: str
    missionReward: Optional[list]

class Invasion:
    """Represents an invasion in the 'Invasions' tab in the navigation screen."""
    id: IdObject
    faction: Faction
    defenderFaction: Faction
    node: str
    count: int
    """The progress of the invasion. Negative numbers indicate attacker is winning, positive numbers for defender. Minimum value is -goal, maximum is goal."""
    goal: int
    locTag: str
    completed: Optional[bool]
    chainId: IdObject
    attackerReward: Reward
    attackerMissionInfo: InvasionMissionInfo
    defenderReward: Reward
    defenderMissionInfo: InvasionMissionInfo
    activation: DateObject
    