from pydantic import BaseModel


class RefreshToken(BaseModel):
    refresh_token: str