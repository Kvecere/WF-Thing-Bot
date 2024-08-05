from typing import Optional
from models.worldState.rawWorldState.common import DateObject, IdObject

class PrimeVaultTraderManifestItem:
    """An item being sold for aya/regal aya from Varzia."""
    itemType: str
    primePrice: Optional[int]
    """The amount of regal aya needed to purchase the item."""
    regularPrice: Optional[int]
    startDate: Optional[DateObject]
    endDate: Optional[DateObject]

class PrimeVaultTraderItemScheduleInfo:
    expiry: DateObject
    featuredItem: str
    previewHiddenUntil: Optional[DateObject]

class PrimeVaultTrader:
    id: IdObject
    activation: DateObject
    initialStartDate: DateObject
    node: str
    """Always TradeHUB1"""
    manifest: list[PrimeVaultTraderManifestItem]
    """The first half of all current items that can be obtained. This includes prime packs, prime warframe sets, most/all of their prime weapons/gear, their noggles, and their relics."""
    expiry: DateObject
    evergreenManifest: list[PrimeVaultTraderManifestItem]
    """The second half of all current items that can be obtained. This includes any remaining prime weapons, as well as all decorations/fashion/etc. That are always available."""
    scheduleInfo: list[PrimeVaultTraderItemScheduleInfo]