class EndlessXpChoice:
    """Represents the list of rewards to choose from for The Circuit."""
    category: str
    """EXC_NORMAL for normal, EXC_HARD for steel path."""
    choices: list[str]
    """The list of rewards to choose from."""