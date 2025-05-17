import uvicorn

from src.settings import settings


def run():
    uvicorn.run(
        "src.api:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True,
    )


if __name__ == "__main__":
    run()
