from typing import Any, AsyncIterator
from fastapi import APIRouter

router = APIRouter()


class StreamingResult:
    def __init__(self, generator):
        self.generator = generator


class ChatKitServer:
    def __init__(self, store):
        self.store = store


@router.get("/")
def test():
    return {"message": "Server is working ✅"}