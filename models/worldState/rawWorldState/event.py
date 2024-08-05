from typing import Optional
from models.worldState.rawWorldState.common import DateObject, IdObject

class EventMessage:
    """Represents an event/announcement seen in the 'News' Section of the orbiter"""
    languageCode: str
    """The 2-character language code."""
    message: str
    """he message to be displayed. Typically either normal text or a path to an internal file."""

class EventLink:
    languageCode: str
    """The 2-character language code."""
    link: str
    """The url to navigate to when clicked on."""

class Event:
    id: IdObject
    messages: list[EventMessage]
    """The url to navigate to when clicked on."""
    prop: str
    links: Optional[list[EventLink]]
    date: DateObject
    eventStartDate: Optional[DateObject]
    eventEndDate: Optional[DateObject]
    imageUrl: Optional[str]
    """The main image used on a Warframe news post???"""
    icon: Optional[str]
    """The internal icon that displays to the left of the message."""
    priority: bool
    mobileOnly: bool
    community: Optional[bool]
    """Whether or not the event shows up in the 'Community' tab."""
    hideEndDateModifier: Optional[bool]
