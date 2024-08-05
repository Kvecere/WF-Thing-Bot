from models.worldState.rawWorldState.common import DateObject


class DailyDeal:
    storeItem: str
    activation: DateObject
    expiry: DateObject
    discount: int
    originalPrice: int
    salePrice: int
    amountTotal: int
    amountSold: int