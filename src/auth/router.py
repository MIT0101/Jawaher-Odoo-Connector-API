## Auth Router
from fastapi import APIRouter, Depends
from src.auth.dtos.user_login_dto import UserLoginDTO
from src.auth.dtos.user_login_response_dto import UserLoginResponseDto
from src.auth.services.auth_service import AuthService

auth_router = APIRouter(
    tags=["Authentication"],
)


# login endpoint
@auth_router.post("/login", response_model=UserLoginResponseDto)
def login(user_login_dto: UserLoginDTO, auth_service: AuthService = Depends(AuthService)):
    return auth_service.authenticate(user_login_dto)
