from models.worldState.rawWorldState.common import DateObject, IdObject, MissionType, SortieBoss


class LiteSortieMission:
    missionType: MissionType
    node: str

class LiteSortie:
    """Represents an Archon Hunt"""
    id: IdObject
    activation: DateObject
    expiry: DateObject
    Reward: str
    seed: int
    boss: SortieBoss
    missions: list[LiteSortieMission]
    """The list of missions in the archon hunt, in order of completion."""