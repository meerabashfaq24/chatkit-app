from fastapi import APIRouter

router = APIRouter()

# Simple test route
@router.get("/")
def test():
    return {"message": "Server is working"}


# Dummy StreamingResult (to stop import errors)
class StreamingResult:
    def __init__(self, content):
        self.content = content


# Dummy StarterChatServer (to fix crashes)
class StarterChatServer:
    def __init__(self, store=None):
        self.store = store

    async def handle(self, message: str):
        return {"response": f"You said: {message}"}