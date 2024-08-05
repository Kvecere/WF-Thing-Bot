from models.worldState.rawWorldState.common import DateObject, GlobalUpgradeOperationType, GlobalUpgradeType, IdObject


class GlobalUpgrade:
    """Represents a temporary upgrade/boost that applies to everyone, such as an event credit booster."""
    id: IdObject
    activation: DateObject
    expiryDate: DateObject
    upgradeType: GlobalUpgradeType
    operationType: GlobalUpgradeOperationType
    value: int
    localizeTag: str
    localizeDescTag: str