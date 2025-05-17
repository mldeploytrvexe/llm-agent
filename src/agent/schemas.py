from typing_extensions import TypedDict


class State(TypedDict):
    message: str
    document_name: str | None
    document_type: str | None
    document_structure: str | None
    is_legal: bool| None