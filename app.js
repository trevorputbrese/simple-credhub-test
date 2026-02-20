const express = require("express");
const cfenv = require("cfenv");

const app = express();
const appEnv = cfenv.getAppEnv();

app.get("/", (req, res) => {
  const service = appEnv.getService("credhub-test");

  if (!service) {
    return res.send(
      "<h1>Service 'credhub-test' not found. Is the app running on Cloud Foundry with a bound service?</h1>"
    );
  }

  const creds = JSON.stringify(service.credentials, null, 2);
  res.send(
    `<h1>Web page loaded. Credhub credentials successfully read.</h1>` +
      `<h2>The Credhub credentials are:</h2>` +
      `<pre>${creds}</pre>`
  );
});

app.listen(appEnv.port, () => {
  console.log(`Server listening on port ${appEnv.port}`);
});
