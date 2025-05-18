

class GlobalStore:
    answer: str | None = None
    mdwn: str | None = None

    chat_history: list[dict] = []