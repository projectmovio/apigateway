import logging

from data.token_store import TokenStore

log = logging.getLogger("apigateway.common")

token_store = TokenStore()


def validate_user(req):
    token = req.headers.get("user_id")
    log.debug("Token: %s", token)

    valid = token_store.validate_token(token)
    return valid
