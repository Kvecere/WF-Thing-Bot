from models.companion.baseManifestItem import BaseManifestItem

class Resource(BaseManifestItem):
    showInInventory: bool
    '''Whether or not resource is shown in the player's inventory'''

class ResourcesManifest:
    exportResources: list[Resource]