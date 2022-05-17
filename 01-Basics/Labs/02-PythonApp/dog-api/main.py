import uvicorn

from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"success": "true"}


@app.get("/dogs/{dog_id}")
def read_dog(dog_id: int, q: Optional[str] = None):
    return {"dog_id": dog_id, "q": q}

