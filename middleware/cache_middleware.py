from flask import request
from cache.cache_store import get, set
from middleware.auth_context import get_auth_context

def cache_response(handler):
    def wrapper(*args, **kwargs):
        key = request.path + "?" + request.query_string.decode()

        cached = get(key)
        if cached:
            return cached

        response = handler(*args, **kwargs)
        set(key, response)
        return response
    return wrapper