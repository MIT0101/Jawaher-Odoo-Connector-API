from fastapi import Depends, HTTPException
from odoo.api import Environment
from odoo.exceptions import AccessDenied

from ..dtos.user_login_dto import UserLoginDTO
from ..dtos.user_login_response_dto import UserLoginResponseDto
from ..schemas.jwt_payload import JWTPayload
from ...jwt_generator.services import jwt_service

from src.config import settings
from src.odoo_integration.providers import get_sudo_env


class AuthService:

    def __init__(self, odoo_env: Environment = Depends(get_sudo_env)):
        self.odoo_env = odoo_env

    def authenticate(self, user_login_dto: UserLoginDTO) -> UserLoginResponseDto:
        user = self.odoo_env["res.users"].sudo().search([("login", "=", user_login_dto.username)])
        if not user:
            raise HTTPException(
                status_code=401,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        try:
            user._login(settings.odoo_db_name, {
                "login": user_login_dto.username,
                "type": "password",
                "password": user_login_dto.password
            }, {"interactive": False})
        except AccessDenied as e:
            raise HTTPException(
                status_code=401,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail="Internal server error",
            )
        jwt_payload = JWTPayload(user_id=user.id, partner_id=user.partner_id.id)
        jwt_token = jwt_service.create_access_token(payload=jwt_payload.model_dump())
        return UserLoginResponseDto(access_token=jwt_token)
