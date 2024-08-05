from models.worldState.rawWorldState.common import DateObject, IdObject


class PVPChallengeInstanceParams:
    n: str
    v: int

class PVPChallengeInstance:
    id: IdObject
    challengeTypeRefID: str
    startDate: DateObject
    endDate: DateObject
    params: list[PVPChallengeInstanceParams]
    isGenerated: bool
    pvpMode: str
    subChallenges: list[IdObject]
    category: str