from models.companion.baseManifestItem import BaseManifestItem

class FusionBundle(BaseManifestItem):
    fusionPoints: int

class FusionBundlesManifest:
    exportFusionBundles: list[FusionBundle]