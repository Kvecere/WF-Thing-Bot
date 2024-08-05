from enum import Enum
from typing import Optional

from pydantic import BaseModel, model_serializer


class IdObject(BaseModel):
	@model_serializer
	def ser_model(self) -> str:
		return self['$oid']

class NumberLongObject:
    numberLong: str

class DateObject:
    date: NumberLongObject

class Job:
    jobType: str
    rewards: str
    masteryReq: str
    minEnemyLevel: int
    maxEnemyLevel: int
    xpAmounts: list[int]
    locationTag: Optional[str]
    isVault: Optional[bool]
    
class RewardItem:
    itemType: str
    itemCount: int

class Reward:
    credits: Optional[int]
    xp: Optional[int]
    items: Optional[list[str]]
    countedItems: Optional[RewardItem]

class Region(int, Enum):
    Mercury = 1
    Venus = 2
    Earth = 3
    Mars = 4
    Jupiter = 5
    Saturn = 6
    Uranus = 7
    Neptune = 8
    Pluto = 9
    Ceres = 10
    Eris = 11
    Sedna = 12
    Europa = 13
    Void = 15
    Phobos = 16
    Deimos = 17
    Lua = 18
    KuvaFortress = 19
    Zariman = 22

class MissionType(str, Enum):
    Rescue = 'MT_RESCUE'
    Survival = 'MT_SURVIVAL'
    Spy = 'MT_INTEL'
    Sabotage = 'MT_SABOTAGE'
    Exterminate = 'MT_EXTERMINATION'
    Capture = 'MT_CAPTURE'
    Excavation = 'MT_EXCAVATE'
    Alchemy = 'MT_ALCHEMY'
    Defense = 'MT_DEFENSE'
    MobileDefense = 'MT_MOBILE_DEFENSE'
    Assassination = 'MT_ASSASSINATION'
    VoidCascade = 'MT_VOID_CASCADE'
    Interception = 'MT_TERRITORY'
    Disruption = 'MT_ARTIFACT'
    Hive = 'MT_HIVE'
    VoidFlood = 'MT_CORRUPTION'
    FreeRoam = 'MT_LANDSCAPE'
    # Volatile
    # Orphix

class Faction(str, Enum):
    Grineer = 'FC_GRINEER'
    Corpus = 'FC_CORPUS'
    Infested = 'FC_INFESTATION'
    Narmer = 'FC_NARMER'

class SortieModifierType(str, Enum):
	RifleOnly = 'SORTIE_MODIFIER_RIFLE_ONLY'
	SniperOnly = 'SORTIE_MODIFIER_SNIPER_ONLY'
	ShotgunOnly = 'SORTIE_MODIFIER_SHOTGUN_ONLY'
	BowOnly = 'SORTIE_MODIFIER_BOW_ONLY'
	SecondaryOnly = 'SORTIE_MODIFIER_SECONDARY_ONLY'
	MeleeOnly = 'SORTIE_MODIFIER_MELEE_ONLY'
	Shields = 'SORTIE_MODIFIER_SHIELDS'
	Eximus = 'SORTIE_MODIFIER_EXIMUS'
	AugmentedEnemyArmor = 'SORTIE_MODIFIER_ARMOR'
	EnergyReduction = 'SORTIE_MODIFIER_LOW_ENERGY'
	Radiation = 'SORTIE_MODIFIER_RADIATION'
	Fire = 'SORTIE_MODIFIER_HAZARD_FIRE'
	CryogenicLeakage = 'SORTIE_MODIFIER_HAZARD_ICE'
	ElectromagneticAnomalies = 'SORTIE_MODIFIER_HAZARD_MAGNETIC'
	EnemyElementalEnhancementBlast = 'SORTIE_MODIFIER_EXPLOSION'
	EnemyElementalEnhancementHeat = 'SORTIE_MODIFIER_FIRE'
	EnemyElementalEnhancementCold = 'SORTIE_MODIFIER_FREEZE'
	EnemyElementalEnhancementToxin = 'SORTIE_MODIFIER_POISON'
	EnemyElementalEnhancementRadiation = 'SORTIE_MODIFIER_RADIATION'
	EnemyElementalEnhancementMagnetic = 'SORTIE_MODIFIER_MAGNETIC'
	EnemyPhysicalEnhancementImpact = 'SORTIE_MODIFIER_IMPACT'
	EnemyPhysicalEnhancementPuncture = 'SORTIE_MODIFIER_PUNCTURE'
	EnemyPhysicalEnhancementSlash = 'SORTIE_MODIFIER_SLASH'

class SortieBoss(str, Enum):
	Vor = 'SORTIE_BOSS_VOR'
	SargasRuk = 'SORTIE_BOSS_RUK'
	VayHek = 'SORTIE_BOSS_HEK'
	TylRegor = 'SORTIE_BOSS_TYL'
	LechKril = 'SORTIE_BOSS_KRIL'
	KelaDeThaym = 'SORTIE_BOSS_KELA'

	NefAnyo = 'SORTIE_BOSS_NEF'
	AladV = 'SORTIE_BOSS_ALAD'
	Raptor = 'SORTIE_BOSS_RAPTOR'

	InfestedAladV = 'SORTIE_BOSS_INFALAD'
	Phorid = 'SORTIE_BOSS_PHORID'
	Lephantis = 'SORTIE_BOSS_LEPHANTIS'

	Nira = 'SORTIE_BOSS_NIRA'
	Boreal = 'SORTIE_BOSS_BOREAL'

class GlobalUpgradeType(str, Enum):
	EventCreditBooster = 'GAMEPLAY_MONEY_REWARD_AMOUNT'


class GlobalUpgradeOperationType(str, Enum):
	Multiply = 'MULTIPLY'


class Tileset(str, Enum):
	GrineerOcean = 'GrineerOceanTileset'
	GrineerOceanAnywhere = 'GrineerOceanTilesetAnywhere'
	GrineerForest = 'GrineerForestTileset'
	GrineerGalleon = 'GrineerGalleonTileset'
	GrineerShipyards = 'GrineerShipyardsTileset'
	GrineerSettlement = 'GrineerSettlementTileset'
	GrineerAsteroid = 'GrineerAsteroidTileset'
	CorpusShip = 'CorpusShipTileset'
	CorpusOutpost = 'CorpusOutpostTileset'
	CorpusIcePlanet = 'CorpusIcePlanetTileset'
	CorpusGasCity = 'CorpusGasCityTileset'
	OrokinMoonCorpus = 'OrokinMoonTilesetCorpus'
	OrokinDerilect = 'OrokinDerelictTileset'
	InfestedCorpusShip = 'InfestedCorpusShipTileset'
	Eidolon = 'EidolonTileset'

class FissureType(str, Enum):
	Lith = 'VoidT1'
	Meso = 'VoidT2'
	Neo = 'VoidT3'
	Axi = 'VoidT4'
	Requiem = 'VoidT5'
	Omnia = 'VoidT6'

