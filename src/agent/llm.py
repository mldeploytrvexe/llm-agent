from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from src.settings import settings


if settings.PROVIDER == "OLLAMA":
    llm = ChatOllama(
        model=settings.MODEL,
        base_url=settings.BASE_URL,
        api_key=settings.OPENAI_API_KEY,
        temperature=settings.TEMPERATURE,
        max_tokens=settings.MAX_TOKENS,
    )
    
elif settings.PROVIDER == "OPENAI":
    llm = ChatOpenAI(
        model=settings.MODEL,
        base_url=f"{settings.BASE_URL}",
        api_key=settings.OPENAI_API_KEY,
        temperature=settings.TEMPERATURE,
        max_tokens=settings.MAX_TOKENS,
    )

else:
    raise ValueError("Неверный провайдер")