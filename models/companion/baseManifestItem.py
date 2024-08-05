class BaseManifestItem:
    uniqueName: str
    '''The relative path to item data.'''

    name: str
    '''The name of the item.'''

    codexSecret: bool | None
    '''Whether or not the entry is hidden in the codex until it's acquired.'''

    excludeFromCodex: bool | None
    '''Whether or not item is hidden from Codex if player does not have it.'''
    
    description: str | None
    '''The description of the item.'''

    parentName: str | None
    '''The relative path to parent item data.'''