from datetime import datetime

import pytz
from pydantic import BaseModel, model_validator, ConfigDict


class CoreSchema(BaseModel):
    """
    Any common logic to be shared by all models goes here
    """

    @model_validator(mode="after")
    def format_datetime(self) -> BaseModel:
        updated_fields = {
            k: v.replace(microsecond=0).astimezone(pytz.timezone('Europe/Moscow'))
            for k, v in self.model_dump().items()
            if isinstance(v, datetime) and not v.tzinfo
        }
        for key, value in updated_fields.items():
            setattr(self, key, value)

        return self

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
    )


class ChatRequest(CoreSchema):
    message: str


class ChatResponse(ChatRequest):
    markdown_str: str | None = None
