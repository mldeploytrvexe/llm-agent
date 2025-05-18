from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.agent.schemas import State
from src.settings import settings
from src.api_schemas import ChatRequest, ChatResponse
from src.logger import logger
from src.agent.graph import app as agent_app
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


@app.post(
    path="/api/chat",
    response_model=ChatResponse
)
async def chat(
    data: ChatRequest
):
    logger.info(f"New message: {data.message}")
    user_text: State = {
        "message": data.message,
        # "document_name": None,
        # "legality": None,
        # "document_structure": None,
        # "markdown_document": None,
        # "next": None
    }
    try:
        _ = agent_app.invoke(user_text)
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
