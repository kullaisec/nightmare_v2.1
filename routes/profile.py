from flask import request
from middleware.cache_middleware import cache_response

@cache_response
def profile():
    name = request.args.get("name", "guest")
    return f"<h1>Hello {name}</h1>"