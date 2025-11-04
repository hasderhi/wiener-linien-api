from fastapi import FastAPI, HTTPException
from transit import fetch_stop_data
from cache import Cache
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


cache = Cache(ttl_seconds=5)

@app.get("/api/stop/{stop_id}")
async def get_stop(stop_id: int):
    cached = cache.get(stop_id)
    if cached:
        return cached

    try:
        data = await fetch_stop_data(stop_id)
        cache.set(stop_id, data)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

from fastapi.responses import FileResponse

@app.get("/api/stops")
async def get_stops():
    return FileResponse("data/stops_grouped.json")

@app.get("/api/ping")
async def ping():
    return {"status": "ok"}
