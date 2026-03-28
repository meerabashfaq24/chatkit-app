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
    class StarterChatServer(ChatKitServer):
    def __init__(self, store):
        super().__init__(store)

    async def respond(self, thread, item, context):
        async def generator():
            yield {
                "type": "message",
                "content": "Hello! Your agent is now working 🚀",
            }

        return StreamingResult(generator())