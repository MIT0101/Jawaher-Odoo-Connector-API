from pydantic import BaseModel


class JWTPayload(BaseModel):
    user_id: int
    partner_id: int
