from google.oauth2.credentials import Credentials
from google.cloud import secretmanager_v1

import base64
import os

GPT3_SECRET_FILE_NAME="openai.secret"
GPT3_SECRET_ID="projects/16255416068/secrets/gpt3-secret/versions/1"

gpt3_secret=None


def get_gpt3_secret():
    global gpt3_secret
    if gpt3_secret:
        return gpt3_secret

    # Check if file already exists
    if os.path.exists(GPT3_SECRET_FILE_NAME):
        with open(GPT3_SECRET_FILE_NAME, "r") as f:
            gpt3_secret = f.readlines()[0]
            return gpt3_secret
    
    # Create a client
    client = secretmanager_v1.SecretManagerServiceClient()

    # Initialize request argument(s)
    request = secretmanager_v1.AccessSecretVersionRequest(
        name=GPT3_SECRET_ID,
    )

    # Make the request
    response = client.access_secret_version(request=request)
    secret = response.payload.data.decode("UTF-8")
    # Save the decoded secret data to a file:
    with open(GPT3_SECRET_FILE_NAME, "w") as f:
        f.write(secret)
    gpt3_secret = secret
    return gpt3_secret


if __name__ == "__main__":
    save_config_json()
