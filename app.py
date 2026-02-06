from flask import Flask
from routes.profile import profile
from routes.admin import admin_panel
from routes.payments import transfer
from oauth.oauth_routes import oauth_start
from oauth.oauth_client import oauth_callback

app = Flask(__name__)

app.add_url_rule("/profile", "profile", profile)
app.add_url_rule("/admin", "admin", admin_panel)
app.add_url_rule("/transfer", "transfer", transfer, methods=["POST"])
app.add_url_rule("/oauth/start", "oauth_start", oauth_start)
app.add_url_rule("/callback", "oauth_callback", oauth_callback)

if __name__ == "__main__":
    app.run(debug=True)