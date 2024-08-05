from typing import Optional
from models.worldState.rawWorldState.common import DateObject, IdObject, Job, Region, Reward



class Goal:
    """Represents an Event seen in the 'Event' tab in the navigation screen."""
    id: IdObject
    activation: DateObject
    expiry: DateObject
    healthPct: float
    """A percentage of attempts/time before the event can no longer be done."""
    victimNode: str
    """The existing start chart node this affects."""
    regions: Optional[list[Region]]
    count: Optional[int]
    goal: Optional[int]
    clanGoal: Optional[list[int]]
    success: int
    personal: Optional[bool]
    community: Optional[bool]
    clampNodeScores: Optional[bool]
    node: Optional[str]
    scoreVar: Optional[str]
    scoreLocTag: Optional[str]
    missionKeyName: Optional[str]
    desc: str
    """The description of the event."""
    toolTip: str
    optionalInMission: Optional[bool]
    upgradeIds: Optional[list[IdObject]]
    icon: str
    tag: str
    reward: Optional[list[Reward] | Reward]
    interimGoals: Optional[list[int]]
    interimRewards: Optional[list[Reward]]
    jobAffiliationTag: str
    jobCurrentVersion: IdObject
    jobs: list[Job]
    jobPreviousVersion: IdObject
    previousJobs: list[Job]
    itemType: Optional[str]


