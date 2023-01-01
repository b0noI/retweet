from google.oauth2.credentials import Credentials
from google.cloud import secretmanager_v1

import base64


def save_config_json():
    # Create a client
    client = secretmanager_v1.SecretManagerServiceClient()

    # Initialize request argument(s)
    request = secretmanager_v1.AccessSecretVersionRequest(
        name="projects/16255416068/secrets/credentials-chatgpt/versions/1",
    )

    # Make the request
    response = client.access_secret_version(request=request)
    secret = response.payload.data.decode("UTF-8")
    # Save the decoded secret data to a file:
    with open('config.json', 'w') as f:
        f.write(secret)
    print("saved")


if __name__ == "__main__":
    save_config_json()
