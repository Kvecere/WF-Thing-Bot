from models.worldState.rawWorldState.common import DateObject, IdObject, MissionType, SortieBoss, SortieModifierType, Tileset

class SortieMission:
    """A mission an a sortie."""
    missionType: MissionType
    modifierType: SortieModifierType
    node: str
    tileset: Tileset

class Sortie:
    """A sortie"""
    id: IdObject
    activation: DateObject
    expiry: DateObject
    Reward: str
    seed: int
    boss: SortieBoss
    extraDrops: list
    variants: list[SortieMission]
    """The list of missions in the sortie, in order of completion."""
    twitter: bool