
import asyncio
import lzma
import json
import httpx
from models.companion.custom import CustomsManifest
from models.companion.drone import DronesManifest
from models.companion.flavour import FlavourManifest
from models.companion.fusionBundle import FusionBundlesManifest
from models.companion.gear import GearManifest
from models.companion.keys import KeysManifest
from models.companion.manifestType import ManifestType
from models.companion.node import RegionsManifest
from models.companion.originStringsGroup import OriginStringsGroup
from models.companion.recipe import RecipesManifest
from models.companion.relicArcane import RelicArcaneManifest
from models.companion.resource import ResourcesManifest
from models.companion.sentinel import SentinelsManifest
from models.companion.sortie import SortieRewardsManifest
from models.companion.upgrade import UpgradesManifest
from models.companion.warframe import WarframesManifest
from models.companion.weapon import *

BaseUrl = 'http://content.warframe.com/PublicExport/Manifest/'

#@cached(cache = TTLCache(1024*10, 30))
async def get_origin_strings():
    originStringsGroup = OriginStringsGroup()
    async with httpx.AsyncClient() as client:

        async def get_lzma():
            return await client.get('https://origin.warframe.com/PublicExport/index_en.txt.lzma')
        
        response = await asyncio.create_task(get_lzma())

        #response = await client.get('https://origin.warframe.com/PublicExport/index_en.txt.lzma')
        if response.status_code >= 200 and response.status_code < 300:
            resultBytes = ''
            a = ''

            data = response.read()
            byt = bytes(data)
            length = len(data)
            stay = True
            while stay:
                stay = False
                try:
                    resultBytes = decompress_lzma(byt[0:length])
                except lzma.LZMAError:
                    length -= 1
                    stay = True
            bytesToStr = resultBytes.decode('utf-8')
            originStringsArr = bytesToStr.splitlines()
            
            originStringsGroup.exportCustoms = next((x for x in originStringsArr if x.startswith('ExportCustoms')), None)
            originStringsGroup.exportDrones = next((x for x in originStringsArr if x.startswith('ExportDrones')), None)
            originStringsGroup.exportFlavour = next((x for x in originStringsArr if x.startswith('ExportFlavour')), None)
            originStringsGroup.exportFusionBundles = next((x for x in originStringsArr if x.startswith('ExportFusionBundles')), None)
            originStringsGroup.exportGear = next((x for x in originStringsArr if x.startswith('ExportGear')), None)
            originStringsGroup.exportKeys = next((x for x in originStringsArr if x.startswith('ExportKeys')), None)
            originStringsGroup.exportRecipes = next((x for x in originStringsArr if x.startswith('ExportRecipes')), None)
            originStringsGroup.exportRegions = next((x for x in originStringsArr if x.startswith('ExportRegions')), None)
            originStringsGroup.exportRelicArcane = next((x for x in originStringsArr if x.startswith('ExportRelicArcane')), None)
            originStringsGroup.exportResources = next((x for x in originStringsArr if x.startswith('ExportResources')), None)
            originStringsGroup.exportSentinels = next((x for x in originStringsArr if x.startswith('ExportSentinels')), None)
            originStringsGroup.exportSortieRewards = next((x for x in originStringsArr if x.startswith('ExportSortieRewards')), None)
            originStringsGroup.exportUpgrades = next((x for x in originStringsArr if x.startswith('ExportUpgrades')), None)
            originStringsGroup.exportWarframes = next((x for x in originStringsArr if x.startswith('ExportWarframes')), None)
            originStringsGroup.exportWeapons = next((x for x in originStringsArr if x.startswith('ExportWeapons')), None)
            originStringsGroup.exportManifest = next((x for x in originStringsArr if x.startswith('ExportManifest')), None)
    return originStringsGroup

def decompress_lzma(data):
    results = []
    while True:
        decomp = lzma.LZMADecompressor(lzma.FORMAT_AUTO, None, None)
        try:
            res = decomp.decompress(data)
        except lzma.LZMAError:
            if results:
                break  # Leftover data is not a valid LZMA/XZ stream; ignore it.
            else:
                raise  # Error on the first iteration; bail out.
        results.append(res)
        data = decomp.unused_data
        if not data:
            break
        if not decomp.eof:
            raise lzma.LZMAError('Compressed data ended before the end-of-stream marker was reached')
    return b''.join(results)


async def get_by_type(manifestType: ManifestType):
    originStringsGroup = await get_origin_strings()
    manifest = BaseManifestItem()
    originString: str = ''
    match manifestType:
        case ManifestType.ExportCustoms:
            manifest = CustomsManifest()
            originString = originStringsGroup.exportCustoms
        case ManifestType.ExportDrones:
            manifest = DronesManifest()
            originString = originStringsGroup.exportDrones
        case ManifestType.ExportFlavour:
            manifest = FlavourManifest()
            originString = originStringsGroup.exportFlavour
        case ManifestType.ExportFusionBundles:
            manifest = FusionBundlesManifest()
            originString = originStringsGroup.exportFusionBundles
        case ManifestType.ExportGear:
            manifest = GearManifest()
            originString = originStringsGroup.exportGear
        case ManifestType.ExportKeys:
            manifest = KeysManifest()
            originString = originStringsGroup.exportKeys
        case ManifestType.ExportRecipes:
            manifest = RecipesManifest()
            originString = originStringsGroup.exportRecipes
        case ManifestType.ExportRegions:
            manifest = RegionsManifest()
            originString = originStringsGroup.exportRegions
        case ManifestType.ExportRelicArcane:
            manifest = RelicArcaneManifest()
            originString = originStringsGroup.exportRelicArcane
        case ManifestType.ExportResources:
            manifest = ResourcesManifest()
            originString = originStringsGroup.exportResources
        case ManifestType.ExportSentinels:
            manifest = SentinelsManifest()
            originString = originStringsGroup.exportSentinels
        case ManifestType.ExportSortieRewards:
            manifest = SortieRewardsManifest()
            originString = originStringsGroup.exportSortieRewards
        case ManifestType.ExportUpgrades:
            manifest = UpgradesManifest()
            originString = originStringsGroup.exportUpgrades
        case ManifestType.ExportWarframes:
            manifest = WarframesManifest()
            originString = originStringsGroup.exportWarframes
        case ManifestType.ExportWeapons:
            manifest = WeaponsManifest()
            originString = originStringsGroup.exportWeapons
        # TODO: the last byte needed for this always gets shaved off in decompression
        case ManifestType.ExportManifest:
            originString = originStringsGroup.exportManifest
    
    if originString is not None:
        async with httpx.AsyncClient() as client:
            async def get_raw_manifest():
                return await client.get(f'{BaseUrl}{originString}')
            
            response = await asyncio.create_task(get_raw_manifest())
            if response.status_code >= 200 and response.status_code < 299:
                manifest = json.loads(response.text, strict=False)

    return manifest

