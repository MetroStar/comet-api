import requests
from fastapi import Depends, HTTPException
from jose.backends import RSAKey
from jose.jwt import decode, get_unverified_header

from app.config import settings


def get_keycloak_jwks():
    keycloak_well_known_url = settings.OIDC_CONFIG_URL
    response = requests.get(keycloak_well_known_url)
    well_known_config = response.json()
    jwks_url = well_known_config["jwks_uri"]
    jwks_response = requests.get(jwks_url)
    jwks = jwks_response.json()
    return jwks["keys"]


def validate_jwt(token: str = Depends(get_keycloak_jwks)):
    header = get_unverified_header(token)
    jwks = get_keycloak_jwks()

    # Find the RSA key with the matching kid in the JWKS
    rsa_key = None
    for key in jwks:
        if key["kid"] == header["kid"]:
            rsa_key = RSAKey(
                key=key["n"], alg=key["alg"], use=key["use"], kid=key["kid"]
            )
            break

    if rsa_key is None:
        raise HTTPException(status_code=401, detail="RSA Key not found in JWKS")

    try:
        payload = decode(token, rsa_key, algorithms=[header["alg"]])
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid JWT token") from Exception

    return payload
