from pydantic import BaseModel

from ..schemas.token_response import TokenResponse


class UserLoginResponseDto(TokenResponse):
    pass
