from typing import Optional

from models.worldState.rawWorldState.common import DateObject


class FlashSale:
    typeName: str
    showInMarket: bool
    hideFromMarket: bool
    supporterPack: bool
    discount: int
    bogoBuy: int
    bogoGet: int
    regularOverride: Optional[int]
    premiumOverride: int
    startDate: DateObject
    endDate: DateObject