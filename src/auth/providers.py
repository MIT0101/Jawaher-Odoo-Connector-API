from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

from src.jwt_generator.services import jwt_service

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_token(token: str = Depends(oauth2_scheme)):
    """Verify JWT token and return payload."""
    return jwt_service.verify_token(token)
