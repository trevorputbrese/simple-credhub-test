# CredHub Test App

A simple Node.js/Express web app for testing CredHub integration with Tanzu Platform for Cloud Foundry. The app uses the `cfenv` package to read a CredHub secret from the `VCAP_SERVICES` environment variable and displays it on a splash page, validating that the secret was successfully bound and injected.

## How It Works

1. A CredHub service instance is created with a secret stored as JSON credentials.
2. The service instance is bound to the app via the `manifest.yml`.
3. When the app is pushed to Cloud Foundry, the platform injects the bound service credentials into the `VCAP_SERVICES` environment variable.
4. The app uses `cfenv` to parse `VCAP_SERVICES`, finds the `credhub-test` service instance, and displays the credentials on the root page.

## Prerequisites

- Access to a Tanzu Platform for Cloud Foundry environment
- The `cf` CLI installed and authenticated
- A CredHub service instance created (see below)

### Create the CredHub Service Instance

**Syntax:**

```bash
cf create-service <service-name> <plan-name> <instance-name> -c '<secret-in-json-format>'
```

**Example:**

```bash
cf cs credhub default credhub-test -c '{"api-key": "12345-abcde"}'
```

This creates a CredHub service instance named `credhub-test` with the credential `{"api-key": "12345-abcde"}`.

## Deploy

Push the app to Cloud Foundry:

```bash
cf push
```

The `manifest.yml` is preconfigured to bind the `credhub-test` service instance to the app.

## Project Structure

| File | Description |
|---|---|
| `app.js` | Express app that uses `cfenv` to read and display CredHub credentials |
| `package.json` | Node.js dependencies (Express, cfenv) |
| `manifest.yml` | Cloud Foundry manifest binding the `credhub-test` service |
| `Procfile` | Runs the app with Node.js |
