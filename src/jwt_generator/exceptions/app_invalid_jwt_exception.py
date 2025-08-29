from jwt import InvalidTokenError


class AppInvalidJWTException(InvalidTokenError):
    """Custom exception for invalid JWT tokens."""
    pass