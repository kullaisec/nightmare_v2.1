from flask import request
from oauth.state_store import valid

def oauth_callback():
    state = request.args.get("state")
    code = request.args.get("code")

    if not valid(state):
        return "Invalid state", 400

    return "Logged in"