from datetime import datetime, timedelta, timezone
from typing import Optional, Dict, Any

import jwt
from jwt import InvalidTokenError

from src.config import settings
from src.jwt_generator.exceptions.app_invalid_jwt_exception import AppInvalidJWTException


def create_access_token(payload: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    """Generate JWT token with user_id, partner_id, and expiration."""
    if expires_delta is None:
        expires_delta = timedelta(days=settings.jwt_expire_days)

    expire = datetime.now(tz=timezone.utc) + expires_delta
    payload.update({"exp": expire})
    encoded_jwt = jwt.encode(payload, settings.jwt_secret_key.get_secret_value(), algorithm=settings.jwt_algorithm)
    return encoded_jwt


def verify_token(token: str) -> Dict[str, Any]:
    """Verify JWT token and return payload."""
    try:
        # PyJWT automatically checks the "exp" claim in the token's payload.
        payload = jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
        return payload
    except InvalidTokenError as e:
        raise AppInvalidJWTException("Invalid JWT token") from e
    except Exception as e:
        raise e
