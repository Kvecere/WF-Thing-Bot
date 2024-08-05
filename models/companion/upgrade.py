from models.companion.baseManifestItem import BaseManifestItem

class UpgradeLevelStat:
    stats: list[str]

class UpgradeValue:
    value: int
    locTag: str

class UpgradeEntry:
    tag: str
    '''The relative path of the tag.'''
    prefixTag: str
    '''The prefix to use in the riven'''
    suffixTag: str
    '''The suffix to use in the riven'''
    upgradeValues: list[UpgradeValue]

class UpgradeComplication:
    fullName: str
    description: str
    overrideTag: str

class UpgradeAvailableChallenge:
    fullName: str
    description: str
    complications: list[UpgradeComplication]

class Upgrade(BaseManifestItem):
    polarity: str
    '''The polarity of upgrade using internal names.'''

    rarity: str
    '''The rarity of the upgrade'''

    baseDrain: int
    '''The base capacity drain'''

    fusionLimit: int
    '''The maximum number of ranks'''

    isUtility: bool | None
    '''Whether or not the upgrade can be fitted in the Exilus slot.'''

    compatName: str | None
    '''The name of the item that the upgrade can be equipped as seen on the card description.'''
    
    type: str
    '''The name of the class of upgrades that it belongs to in all caps.'''
    
    description: list[str]
    subtype: str
    '''The relative path to the Warframe (for augment mods)'''

    levelStats: list[UpgradeLevelStat] | None
    upgradeEntries: list[UpgradeEntry]
    availableChallenges: list[UpgradeAvailableChallenge]

class ModSet:
    uniqueName: str
    '''The relative path to item data.'''

    numUpgradesInSet: int
    '''The number of mods in the set'''

    buffSet: bool | None
    stats: list[str]

class UpgradesManifest:
    exportUpgrades: list[Upgrade]
    exportModSet: list[ModSet]
    exportAvionics: list[Upgrade]
    exportFocusUpgrades: list[Upgrade]