from typing import TypedDict
from src.api_schemas import CoreSchema


class Legality(CoreSchema):
    is_legal: bool
    reason: str | None


class State(TypedDict):
    message: str
    document_name: str
    legality: Legality
    document_structure: str
    markdown_document: str
    next: str
