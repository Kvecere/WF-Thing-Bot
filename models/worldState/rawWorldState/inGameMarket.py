from typing import Optional


class InGameMarketLandingPageCategory:
    
    categoryName: str
    name: str
    icon: str
    addToMenu: Optional[bool]
    items: list[str]

class InGameMarketLandingPage:
    categories: list[InGameMarketLandingPageCategory]

class InGameMarket:
    """Represents the initial page of the warframe market page."""
    landingPage: InGameMarketLandingPage