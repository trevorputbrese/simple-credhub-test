import json
import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    vcap_services = os.environ.get("VCAP_SERVICES")

    if not vcap_services:
        return "<h1>VCAP_SERVICES not found. Is the app running on Cloud Foundry with a bound service?</h1>"

    services = json.loads(vcap_services)

    # Search all service types for our service instance by name
    for service_type, instances in services.items():
        for instance in instances:
            if instance.get("name") == "credhub-test":
                creds = json.dumps(instance.get("credentials", {}), indent=2)
                return (
                    f"<h1>Web page loaded. Credhub credentials successfully read.</h1>"
                    f"<h2>The Credhub credentials are:</h2>"
                    f"<pre>{creds}</pre>"
                )

    return "<h1>Service 'credhub-test' not found in VCAP_SERVICES.</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
