from models.companion.baseManifestItem import BaseManifestItem

class ColorValue:
    value: str
    '''The hex color value'''

class Flavour(BaseManifestItem):
    hexColours: list[ColorValue]

class FlavourManifest:
    exportFlavour: list[Flavour]