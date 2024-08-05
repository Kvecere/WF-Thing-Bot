from typing import Optional
from models.worldState.rawWorldState.common import DateObject, IdObject

class VoidTraderManifestItem:
    itemType: str
    primePrice: int
    """The number of ducats it costs."""
    regularPrice: int
    """The number of credits it costs."""

class VoidTrader:
    """Represents information about the current/next location of Baro Ki'teer"""
    id: IdObject
    activation: DateObject
    expiry: DateObject
    character: str
    """Always misspelled Baro'Ki Teel"""
    node: str
    """TennoConHUB2 if it's TennoCon baro, otherwise the node he's current at or will be at."""
    manifest: Optional[list[VoidTraderManifestItem]]