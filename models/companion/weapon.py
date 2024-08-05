from models.companion.baseManifestItem import BaseManifestItem

class Weapon(BaseManifestItem):
    damagePerShot: list[float]
    """A list of numbers indicating how much damage is dealt per shot/hit by status type"""

    totalDamage: float
    """The total amount of damage the weapon does"""

    criticalChance: float
    criticalMultiplier: float
    procChance: float
    """The status chance of the weapon."""

    fireRate: float
    masteryReq: int
    productCategory: str
    """The category or subcategory the weapon falls into, such as Rifles, Shotguns, Bows, etc."""

    excludeFromCodex: bool | None
    """Whether the weapon should never show up in the codex"""

    slot: int
    accuracy: float
    omegaAttenuation: float
    """The riven disposition of the weapon"""

    # Non-Melee Weapons
    noise: str
    trigger: str
    magazineSize: int
    reloadTime: float
    multishot: int

    # Melee Weapons
    blockingAngle: int
    comboDuration: int
    followThrough: float
    range: float
    slamAttack: int
    slamRadialDamage: int
    slamRadius: int
    slideAttack: int
    heavyAttackDamage: int
    heavySlamAttack: int
    heavySlamRadialDamange: int
    heavySlamRadius: int
    windUp: float

class WeaponsManifest:
    exportWeapons: list[Weapon]
    exportRailjackWeapons: list[Weapon]