from jwt_payload import JWTPayload


class DecodedJWTPayload(JWTPayload):
    exp: int  # Unix timestamp of expiration
