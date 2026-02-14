import os
import httpx
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

if not PEXELS_API_KEY:
    raise Exception("PEXELS_API_KEY is missing in environment variables.")

PHOTOS_URL = "https://api.pexels.com/v1/search"
VIDEOS_URL = "https://api.pexels.com/videos/search"

app = FastAPI(
    title="Broken Wallpapers & Videos API",
    description="Search HD wallpapers and videos using Pexels.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Broken Wallpapers & Videos API 🎨🎬",
        "usage": "/search?query=anime"
    }

@app.get("/search")
async def search(query: str = Query(..., min_length=1)):
    headers = {"Authorization": PEXELS_API_KEY}

    async with httpx.AsyncClient(timeout=30.0) as client:
        # Search photos
        photo_resp = await client.get(PHOTOS_URL, params={"query": query, "per_page": 20}, headers=headers)
        # Search videos
        video_resp = await client.get(VIDEOS_URL, params={"query": query, "per_page": 10}, headers=headers)

    if photo_resp.status_code != 200:
        raise HTTPException(status_code=photo_resp.status_code, detail="Failed to fetch photos from Pexels.")

    if video_resp.status_code != 200:
        raise HTTPException(status_code=video_resp.status_code, detail="Failed to fetch videos from Pexels.")

    photos = photo_resp.json().get("photos", [])
    videos = video_resp.json().get("videos", [])

    return {
        "query": query,
        "wallpapers": [
            {
                "id": p["id"],
                "url": p["src"]["original"],
                "preview": p["src"]["medium"],
                "photographer": p["photographer"]
            }
            for p in photos
        ],
        "videos": [
            {
                "id": v["id"],
                "url": v["video_files"][0]["link"],
                "quality": v["video_files"][0]["quality"],
                "preview": v["image"]
            }
            for v in videos
        ]
    }
