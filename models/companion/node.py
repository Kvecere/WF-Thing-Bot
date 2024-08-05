class Region:
    uniqueName: str
    '''The relative path to item data.'''
    
    name: str
    '''The name of the item.'''

    systemIndex: int
    '''Region index'''

    systemName: str
    '''Localized region name'''

    nodeType: int
    '''Node type (all entries have this at 0 for some reason)'''

    masteryReq: int
    '''Mastery Rank requirement'''

    missionIndex: int
    '''Mission type index'''

    factionIndex: int
    '''Controlling faction index'''

    minEnemyLevel: int
    '''Starting enemy level'''

    maxEnemyLevel: int
    '''Maximum enemy level'''

class RegionsManifest:
    exportRegions: list[Region]