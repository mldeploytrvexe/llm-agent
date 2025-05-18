from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.SP.action import run_SP, clear_history
from src.settings import settings
from src.api_schemas import ChatRequest, ChatResponse
from src.mock import mock_markdown
from src.logger import logger
from src.agent.graph import document_name_node
from src.global_store import GlobalStore



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

state = {}


@app.post(
    path="/api/chat",
    response_model=ChatResponse
)
async def chat(
    data: ChatRequest
):
    logger.info(f"New message: {data.message}")
    user_text = {"message": data.message}
    try:
        _ = document_name_node(user_text)
        logger.info(GlobalStore.answer)
        return ChatResponse(
            message=GlobalStore.answer,
            markdown_str=GlobalStore.mdwn
        )
    except Exception as e:
        logger.error(str(e))
        return ChatResponse(
            message="У меня что-то сломалось по-моему",
        )


@app.post(
    path="/api/chat_v2",
    response_model=ChatResponse
)
async def chat_v2(
    data: ChatRequest
):
    logger.info(f"New message: {data.message}")
    try:
        response = run_SP(data.message)
        
        return response
    except Exception as e:
        logger.error(str(e.__repr__()))
        return ChatResponse(
            message="У меня что-то сломалось по-моему",
        )


@app.post(
    path="/api/chat_v2/clear"
)
async def clear():
    logger.info('Cleared history')
    clear_history()
