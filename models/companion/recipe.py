class Ingredient():
    itemType: str
    itemCount: int
    productCategory: str | None

class Recipe():
    uniqueName: str
    '''The relative path to item data'''

    resultType: str
    '''The relative path to the resultant item data'''

    buildPrice: int
    '''The credit cost to build the item'''

    buildTime: int
    '''The required time to build in seconds'''

    skipBuildTimePrice: int
    '''The platinum cost to skip build time'''

    consumeOnUse: bool
    '''Denotes whether or not the blueprint is reusable'''

    num: int
    '''Number of that particular item built (?)'''

    codexSecret: bool
    '''Whether or not the entry is hidden in the codex until it's acquired.'''

    primeSellingPrice: int
    '''The amount of ducats gained when traded to Ducat kiosk in relays (only for Prime blueprints)'''

    ingredients: list[Ingredient]
    '''The blueprint requirements'''

    secretIngredients: list[Ingredient]
    '''The hidden blueprint requirements'''

class RecipesManifest:
    exportRecipes: list[Recipe]