from models.worldState.rawWorldState.common import DateObject, FissureType, IdObject


class VoidStorm:
    """Represents a void storm"""
    id: IdObject
    node: str
    activation: DateObject
    expiry: DateObject
    activeMissionTier: FissureType