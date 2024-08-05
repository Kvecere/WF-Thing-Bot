from models.companion.baseManifestItem import BaseManifestItem

class WarframeAbility:
    abilityUniqueName: str
    abilityName: str
    description: str

class Warframe(BaseManifestItem):
    health: int
    '''Base health value'''
    shield: int
    '''Base shield value'''
    armor: int
    '''Base armor value'''
    stamina: int
    '''Base stamina value (deprecated)'''
    power: int
    '''Base energy value'''
    masteryReq: int
    '''The mastery rank requirement'''
    sprintSpeed: float
    '''Base sprint speed'''
    passiveDescription: str
    '''The localized passive description'''
    exalted: list[str]
    '''The exalted weapons associeted with the avatar'''
    abilities: list[WarframeAbility]
    productCategory: str
    '''The avatar's product category'''

class WarframeAbility:
    abilityUniqueName: str
    abilityName: str
    description: str

class WarframesManifest:
    exportWarframes: list[Warframe]
    exportAbilities: list[WarframeAbility]
