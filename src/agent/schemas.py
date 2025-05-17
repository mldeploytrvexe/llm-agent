from typing_extensions import TypedDict
from pydantic import BaseModel



class Legality(BaseModel):
    is_legal: bool
    reason: str | None

class State(TypedDict):
    message: str
    document_name: str | None
    legality: Legality
    document_structure: str | None
    markdown_document: str | None