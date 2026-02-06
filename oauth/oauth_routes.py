from flask import request, redirect
from oauth.state_store import save
from oauth.provider_registry import PROVIDERS

def oauth_start():
    provider = request.args.get("provider")
    state = request.args.get("state")  
    save(state)

    return redirect(
        f"{PROVIDERS[provider]}"
        f"?client_id=abc"
        f"&redirect_uri=http://localhost/callback"
        f"&state={state}"
    )