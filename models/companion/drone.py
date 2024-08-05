from models.companion.baseManifestItem import BaseManifestItem

class Drone(BaseManifestItem):
    binCount: int
    '''The number of unique resources the extractor is able to collect'''

    binCapacity: int
    '''The number of rolls for a particular resource (?)'''

    fillRate: int
    '''The number of hours before the extractor can be reclaimed/undeployed to collect resources.'''

    durability: int
    '''The amount of health that the extactor has before being destroyed'''

    repairRate: int
    '''The amount of health restored per hour when not deployed'''

    capacityMultiplier: list[int]
    '''The resource gain multiplier in the order of common, uncommon, rare, and research resources'''

    specialties: list
    '''Unknown'''

class DronesManifest():
    exportDrones: list[Drone]