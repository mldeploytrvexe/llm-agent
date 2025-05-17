from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.settings import settings
from src.api_schemas import ChatRequest, ChatResponse
from src.mock import mock_markdown
from src.logger import logger

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


@app.post(
    path="/chat",
    response_model=ChatResponse
)
async def chat(
    data: ChatRequest
):
    logger.info(f"New message: {data.message}")
    try:
        return ChatResponse(
            message="Думаю... Ответ будет справа",
            markdown_str=mock_markdown
        )
    except Exception as e:
        logger.error(str(e))
        return ChatResponse(
            message="У меня что-то сломалось по-моему",
        )

