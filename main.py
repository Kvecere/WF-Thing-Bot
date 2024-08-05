from async_lru import alru_cache
from fastapi import FastAPI, status
import uvicorn
from models.companion.manifestType import ManifestType
from services import worldState
import services.companion as companion

app = FastAPI()

@app.get('/')
def a():
    return None

@app.get('/customs', status_code=status.HTTP_200_OK)
async def get_customs():
    return await companion.get_by_type(ManifestType.ExportCustoms)

@app.get('/drones', status_code=status.HTTP_200_OK)
async def get_drones():
    return await companion.get_by_type(ManifestType.ExportDrones)

@app.get('/flavours', status_code=status.HTTP_200_OK)
async def get_flavours():
    return await companion.get_by_type(ManifestType.ExportFlavour)

@app.get('/fusionBundles', status_code=status.HTTP_200_OK)
async def get_fusion_bundles():
    return await companion.get_by_type(ManifestType.ExportFusionBundles)

@app.get('/gear', status_code=status.HTTP_200_OK)
async def get_gear():
    return await companion.get_by_type(ManifestType.ExportGear)

@app.get('/keys', status_code=status.HTTP_200_OK)
async def get_keys():
    return await companion.get_by_type(ManifestType.ExportKeys)

@app.get('/recipes', status_code=status.HTTP_200_OK)
async def get_recipes():
    return await companion.get_by_type(ManifestType.ExportRecipes)

@app.get('/regions', status_code=status.HTTP_200_OK)
async def get_regions():
    return await companion.get_by_type(ManifestType.ExportRegions)

@app.get('/relicArcane', status_code=status.HTTP_200_OK)
async def get_relics_arcanes():
    return await companion.get_by_type(ManifestType.ExportRelicArcane)

@app.get('/resources', status_code=status.HTTP_200_OK)
async def get_resources():
    return await companion.get_by_type(ManifestType.ExportResources)

@app.get('/sentinels', status_code=status.HTTP_200_OK)
async def get_sentinels():
    return await companion.get_by_type(ManifestType.ExportSentinels)

@app.get('/sortieRewards', status_code=status.HTTP_200_OK)
async def get_sortie_rewards():
    return await companion.get_by_type(ManifestType.ExportSortieRewards)

@app.get('/upgrades', status_code=status.HTTP_200_OK)
async def get_upgrades():
    return await companion.get_by_type(ManifestType.ExportUpgrades)

@app.get('/warframes', status_code=status.HTTP_200_OK)
async def get_warframes():
    return await companion.get_by_type(ManifestType.ExportWarframes)

@app.get("/weapons", status_code=status.HTTP_200_OK)
async def get_weapons():
    return await companion.get_by_type(ManifestType.ExportWeapons)

@app.get('/manifest', status_code=status.HTTP_200_OK)
async def get_manifest():
    return await companion.get_by_type(ManifestType.ExportManifest)



@app.get('/worldState', status_code=status.HTTP_200_OK)
async def get_world_state():
    return await worldState.get_world_state()

if __name__ == "__main__":
    uvicorn.run(app)