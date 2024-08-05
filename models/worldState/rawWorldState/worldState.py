from pydantic.dataclasses import dataclass
from models.worldState.rawWorldState.activeMission import ActiveMission
from models.worldState.rawWorldState.alert import Alert
from models.worldState.rawWorldState.dailyDeal import DailyDeal
from models.worldState.rawWorldState.endlessXpChoice import EndlessXpChoice
from models.worldState.rawWorldState.event import Event
from models.worldState.rawWorldState.featuredGuild import FeaturedGuild
from models.worldState.rawWorldState.flashSale import FlashSale
from models.worldState.rawWorldState.globalUpgrade import GlobalUpgrade
from models.worldState.rawWorldState.goal import Goal
from models.worldState.rawWorldState.inGameMarket import InGameMarket
from models.worldState.rawWorldState.invasion import Invasion
from models.worldState.rawWorldState.libraryInfo import LibraryInfo
from models.worldState.rawWorldState.liteSortie import LiteSortie
from models.worldState.rawWorldState.nodeOverride import NodeOverride
from models.worldState.rawWorldState.primeAccessAvailability import PrimeAccessAvailability
from models.worldState.rawWorldState.primeVaultTrader import PrimeVaultTrader
from models.worldState.rawWorldState.pvpChallengeInstance import PVPChallengeInstance
from models.worldState.rawWorldState.seasonInfo import SeasonInfo
from models.worldState.rawWorldState.sortie import Sortie
from models.worldState.rawWorldState.syndicateMission import SyndicateMission
from models.worldState.rawWorldState.voidStorm import VoidStorm
from models.worldState.rawWorldState.voidTrader import VoidTrader

class HubEvent:
    pass
class PersistentEnemy:
    pass
class PVPAlternativeMode:
    pass
class PVPActiveTournament:
    pass
class ConstructionProject:
    pass
class TwitchPromo:
    pass
class ExperimentRecommended:
    pass

@dataclass(config=dict(arbitrary_types_allowed=True))
class WorldState:
    worldSeed: str
    version: float
    mobileVersion: str
    time: int
    events: list[Event]
    goals: list[Goal]
    alerts: list[Alert]
    sorties: list[Sortie]
    liteSorties: list[LiteSortie]
    syndicateMissions: list[SyndicateMission]
    activeMissions: list[ActiveMission]
    globalUpgrades: list[GlobalUpgrade]
    flashSales: list[FlashSale]
    inGameMarket: InGameMarket
    invasions: list[Invasion]
    hubEvents: list[HubEvent]
    nodeOverrides: list[NodeOverride]
    voidTraders: list[VoidTrader]
    primeVaultTraders: list[PrimeVaultTrader]
    voidStorms: list[VoidStorm]
    primeAccessAvailability: PrimeAccessAvailability
    primeVaultAvailabilities: list[bool]
    """Always 5 false entries"""
    primeTokenAvailability: bool
    """Always true"""
    dailyDeals: list[DailyDeal]
    libraryInfo: list[LibraryInfo]
    pvpChallengeInstances: list[PVPChallengeInstance]
    persistentEnemies: list[PersistentEnemy]
    pvpAlternativeModes: list[PVPAlternativeMode]
    pvpActiveTournaments: list[PVPActiveTournament]
    persistentEnemies: list[PersistentEnemy]
    projectPct: list[float]
    constructionProjects: list[ConstructionProject]
    twitchPromos: list[TwitchPromo]
    experimentRecommended: list[ExperimentRecommended]
    endlessXpChoices: list[EndlessXpChoice]
    forceLogoutVersion: int
    """Always 0"""
    featuredGuilds: list[FeaturedGuild]
    seasonInfo: SeasonInfo
    tmp: str


