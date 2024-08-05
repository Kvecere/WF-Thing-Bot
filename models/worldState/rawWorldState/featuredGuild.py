from typing import Optional
from models.worldState.rawWorldState.common import IdObject


class FeaturedGuildHiddenPlatforms:
    platformSwitch: bool
    platformIos: bool
    platformCrossPlatform: bool

class FeaturedGuild:
    """Represents a clan featured on the star chart."""
    id: IdObject
    name: str
    tier: int
    allianceId: IdObject
    originalPlatform: Optional[int]
    emblem: bool
    hiddenPlatforms: Optional[FeaturedGuildHiddenPlatforms]