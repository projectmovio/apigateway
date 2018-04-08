from data.token_store import TokenStore
from utils.log import Log

log = Log().get_logger("gateway.utils.common")
token_store = TokenStore()


def validate_user(req):
    token = req.headers.get("user_id")
    log.debug("Token: %s", token)

    valid = token_store.validate_token(token)
    if not valid:
        return False
    return True
