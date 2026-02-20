import json
import os

from cfenv import AppEnv
from flask import Flask

app = Flask(__name__)
env = AppEnv()


@app.route("/")
def index():
    service = env.get_service(name="credhub-test")

    if not service:
        return "<h1>Service 'credhub-test' not found. Is the app running on Cloud Foundry with a bound service?</h1>"

    creds = json.dumps(service.credentials, indent=2)
    return (
        f"<h1>Web page loaded. Credhub credentials successfully read.</h1>"
        f"<h2>The Credhub credentials are:</h2>"
        f"<pre>{creds}</pre>"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
