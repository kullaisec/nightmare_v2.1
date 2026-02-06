from flask import request

def csrf_protect():
    token = request.headers.get("X-CSRF-Token")
    cookie = request.cookies.get("session")

    return token == cookie