from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.settings import settings

app = FastAPI(
    debug=True,
    title=settings.TITLE,
    version=settings.TITLE,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(path="/status")
async def status():
    return True
