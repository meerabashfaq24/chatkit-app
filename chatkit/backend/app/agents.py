from typing import Any, AsyncIterator, List


class AgentContext:
    def __init__(self, thread, store, request_context):
        self.thread = thread
        self.store = store
        self.request_context = request_context


async def simple_to_agent_input(items: List[Any]) -> str:
    messages = []
    for item in items:
        if hasattr(item, "content"):
            messages.append(str(item.content))
    return "\n".join(messages)


async def stream_agent_response(context, result) -> AsyncIterator[dict]:
    # VERY IMPORTANT: this is a working minimal response
    yield {
        "type": "message",
        "content": "Hello! Your agent is now working ✅",
    }