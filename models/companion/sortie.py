from models.companion.baseManifestItem import BaseManifestItem

class SortieReward:
    rewardName: str
    itemCount: int
    probability: float
    rarity: str
    tier: int

class NightwaveChallenge(BaseManifestItem):
    uniqueName: str
    '''The relative path to item data.'''

    name: str
    '''The name of the item.'''

    description: str | None
    '''The description of the item.'''

    standing: int
    '''The amount of standing given upon completing the challenge'''

    required: int
    '''The amount of the task required to do (relates to COUNT within the description). Defaults to 1'''

class NightwaveReward(BaseManifestItem):
    components: list[str] | None
    '''The names of items that are part of the reward'''

class NightwaveExport:
    affiliationTag: str
    '''The name of the current nightwave'''
    challenges: list[NightwaveChallenge]
    rewards: list[NightwaveReward]

class RailjackNode(BaseManifestItem):
    pass

class RailjackNodeExport:
    nodes: list[RailjackNode]

class RailjackIntrinsicRank:
    name: str
    description: str

class RailjackIntrinsic:
    name: str
    ranks: list[RailjackIntrinsicRank]

class MiscallaneousItem(BaseManifestItem):
    pass

class SortieRewardsManifest:
    exportSortieRewards: list[SortieReward]
    exportNightwave: NightwaveExport
    exportRailjack: RailjackNodeExport
    exportIntrinsics: list[RailjackIntrinsic]
    exportOther: list[MiscallaneousItem]