from middleware.cache_middleware import cache_response
from flask import request

@cache_response
def admin_panel():
    if request.headers.get("Authorization") != "Bearer admin":
        return "Forbidden", 403
    return "ADMIN SECRETS"