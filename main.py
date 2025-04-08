from typing import Any

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.core.dependencies import get_tron_client
from src.tron.api.v1.tron import tron_router


async def lifespan() -> Any:
    yield
    get_tron_client().close()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tron_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
