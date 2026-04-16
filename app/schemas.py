from pydantic import BaseModel

class APIKeyResponse(BaseModel):
    key: str

    class Config:
        from_attributes = True