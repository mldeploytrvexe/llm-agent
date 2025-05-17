from pydantic import BaseModel, ConfigDict



class CoreModel(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
    )

class Legality(CoreModel):
    is_legal: bool
    reason: str | None

class State(CoreModel):
    message: str
    document_name: str | None = None
    legality: Legality | None = None
    document_structure: str | None = None
    markdown_document: str | None = None
    next: str | None = None