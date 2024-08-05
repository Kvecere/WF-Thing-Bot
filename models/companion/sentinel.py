from models.companion.baseManifestItem import BaseManifestItem

class Sentinel(BaseManifestItem):
    health: int
    shield: int
    armor: int
    stamina: int
    power: int
    masteryReq: int
    productCategory: str

class SentinelsManifest():
    exportSentinels: list[Sentinel]