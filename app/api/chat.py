import json
from collections.abc import AsyncGenerator

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.config import get_settings
from app.schemas import ChatRequest
from app.services.llm import build_chat_model

router = APIRouter(prefix="/api/v1", tags=["chat"])


def sse(event: str, data: dict) -> str:
    return f"event: {event}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n"


async def event_stream(request: ChatRequest) -> AsyncGenerator[str, None]:
    settings = get_settings()
    if not settings.model_api_key:
        yield sse("error", {"message": "MODEL_API_KEY is not configured"})
        return

    try:
        model = build_chat_model()
    except Exception as exc:  # pragma: no cover - configuration error path
        yield sse("error", {"message": str(exc)})
        return

    yield sse(
        "meta",
        {
            "session_id": request.session_id,
            "model": settings.model_name,
            "context": [],
            "sources": [],
        },
    )

    try:
        async for chunk in model.astream(request.message):
            if chunk.content:
                yield sse("delta", {"text": chunk.content})
        yield sse("done", {"status": "completed"})
    except Exception as exc:  # pragma: no cover - runtime error path
        yield sse("error", {"message": str(exc)})


@router.post("/chat")
async def chat(request: ChatRequest) -> StreamingResponse:
    return StreamingResponse(
        event_stream(request),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )

