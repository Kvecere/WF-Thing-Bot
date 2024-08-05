from typing import Optional
from models.worldState.rawWorldState.common import DateObject, IdObject, Job


class SyndicateMission:
    """Represents a syndicate and all of its missions."""
    id: IdObject
    activation: DateObject
    expiry: DateObject
    tag: str
    seed: int
    nodes: Optional[list[str]]
    """The list of nodes that have syndicate missions. Applies to the main 6."""
    jobs: Optional[Job]
    """The list of jobs (aka missions) to pick from the syndicate. Applies to open world-type syndicates."""