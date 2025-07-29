import asyncio
import aiohttp
from tqdm.asyncio import tqdm_asyncio
import pandas as pd

API_URL = "https://api.postcodes.io/postcodes?lon={lon}&lat={lat}"

async def fetch_postcode(session, lat, lon):
    try:
        async with session.get(API_URL.format(lat=lat, lon=lon), timeout=10) as resp:
            data = await resp.json()
            result = data.get("result")
            return {
                "latitude": lat,
                "longitude": lon,
                "postcode": result.get("postcode") if result else None,
                "admin_district": result.get("admin_district") if result else None,
                "region": result.get("region") if result else None,
                "quality": result.get("quality") if result else None,
            }
    except Exception as e:
        return {
            "latitude": lat,
            "longitude": lon,
            "postcode": None,
            "admin_district": None,
            "region": None,
            "quality": None,
            "error": str(e)
        }

async def enrich_all(coords):
    results = []
    sem = asyncio.Semaphore(10)
    async with aiohttp.ClientSession() as session:
        async def sem_fetch(lat, lon):
            async with sem:
                return await fetch_postcode(session, lat, lon)
        tasks = [sem_fetch(row.latitude, row.longitude) for row in coords.itertuples()]
        results = await tqdm_asyncio.gather(*tasks)
    return results

def enrich_coordinates(df):
    results = asyncio.run(enrich_all(df[["latitude", "longitude"]]))
    return pd.DataFrame(results)