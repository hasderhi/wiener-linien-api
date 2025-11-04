import httpx
from datetime import datetime, timezone
from typing import Dict, Any, List

BASE_URL = "https://www.wienerlinien.at/ogd_realtime/monitor"

def parse_departures(data: Dict[str, Any]) -> Dict[str, Any]:
    monitor = data["data"]["monitors"][0]
    props = monitor["locationStop"]["properties"]

    # Determine stop ID (RBL)
    stop_id = props.get("attributes", {}).get("rbl")
    if stop_id is None:
        stop_id = props.get("stopId")  # fallback

    stop = {
        "id": stop_id,
        "name": props.get("title"),
        "coords": [
            monitor["locationStop"]["geometry"]["coordinates"][0],
            monitor["locationStop"]["geometry"]["coordinates"][1]
        ]
    }

    departures = []
    for line in monitor.get("lines", []):
        for dep in line.get("departures", {}).get("departure", []):
            departures.append({
                "line": line.get("name"),
                "direction": line.get("towards"),
                "planned": dep["departureTime"].get("timePlanned"),
                "countdown": dep["departureTime"].get("countdown"),
                "barrier_free": line.get("barrierFree", False)
            })

    traffic = []
    for msg in data["data"].get("trafficInfos", []):
        traffic.append({
            "type": msg.get("name") or msg.get("refTrafficInfoNames"),
            "msg": msg.get("title"),
            "start": msg.get("time", {}).get("start"),
            "end": msg.get("time", {}).get("end")
        })

    return {
        "stop": stop,
        "departures": sorted(departures, key=lambda x: x["countdown"] or 999),
        "traffic": traffic
    }

async def fetch_stop_data(stop_id: int) -> Dict[str, Any]:
    async with httpx.AsyncClient() as client:
        url = f"{BASE_URL}?stopId={stop_id}&activateTrafficInfo=stoerunglang"
        resp = await client.get(url)
        resp.raise_for_status()
        return parse_departures(resp.json())

