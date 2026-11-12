# DevOps Activity 3B – Secret Manager

A hands-on DevOps project focused on secure local secret handling, Git security practices, and Google Cloud Logging and Monitoring.

## Project Overview

This project demonstrates how to:
- Store sensitive configuration values in a local `.env` file.
- Prevent secrets from being committed to Git using `.gitignore`.
- Read environment variables securely using Python.
- Maintain project source code in Git and GitHub.
- Explore Google Cloud Logging and Monitoring.

## Project Structure

```text
Activity3B-SecretManager/
├── .gitignore
├── read_secret.py
└── .env                 # Local only – not committed
```

## Technologies Used

- Python
- Git and GitHub
- Python dotenv
- Google Cloud Logging
- Google Cloud Monitoring
- Google Cloud Secret Manager (cloud integration pending)

## Local Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/rahul010699-design/Activity3B-SecretManager.git
   ```

2. Navigate into the project:

   ```bash
   cd Activity3B-SecretManager
   ```

3. Install the required dependency:

   ```bash
   pip install python-dotenv
   ```

4. Create a local `.env` file and add your own environment variables.

5. Run the Python script:

   ```bash
   python read_secret.py
   ```

## Security Practices

- `.env` is excluded through `.gitignore`.
- Secret values must never be committed to GitHub.
- Only non-sensitive source files are tracked.
- Never publish API keys, passwords, or credentials.

## Google Cloud Status

Local secret handling and GitHub integration have been completed.

Google Cloud Secret Manager API activation is currently pending because billing is disabled for the project.

Cloud Logging audit logs have been verified, and a Monitoring dashboard has been configured. CPU metric data and a working uptime check are still pending verification.

## Repository

[Activity3B-SecretManager](https://github.com/rahul010699-design/Activity3B-SecretManager)
