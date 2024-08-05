from models.companion.baseManifestItem import BaseManifestItem

class RelicReward:
    rewardName: str
    '''The relative path to the reward item'''
    
    rarity: str
    '''The rarity of the item in the relic'''

    tier: int
    '''The tier of the reward. Always 0'''

    itemCount: int
    '''The number of this reward that is given when chosen'''

class Relic(BaseManifestItem):
    relicRewards: list[RelicReward]

class ArcaneRankStat:
    stats: list[str]
    '''The stats of the arcane for the given rank'''

class Arcane:
    levelStats: list[ArcaneRankStat] | None
    '''The stats of the arcane for all ranks'''

class RelicArcaneManifest:
    exportRelicArcane: list[Relic | Arcane]