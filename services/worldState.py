import asyncio
import json
import httpx

from models.worldState.rawWorldState.worldState import WorldState

async def get_world_state():
    worldState: WorldState = WorldState()
    async with httpx.AsyncClient() as client:
        async def get_state():
            return await client.get('https://content.warframe.com/dynamic/worldState.php')
        
        response = await asyncio.create_task(get_state())
        if response.status_code >= 200 and response.status_code < 299:
            worldState = json.loads(response.text, strict=False, cls=WorldState)
            a = WorldState(**worldState)
            print(worldState)
    return worldState