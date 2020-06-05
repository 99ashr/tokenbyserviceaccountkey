from google.auth.transport import requests
from google.oauth2 import service_account


def bearer_token(filename, credential_scope):
    credentials = service_account.Credentials.from_service_account_file(
        filename, scopes=credential_scopes
    )
    credentials.refresh(requests.Request())
    return credentials.token


credential_scopes = ["https://www.googleapis.com/auth/cloud-platform"]
service_account_file = "./yash-rnd-031df0bc7bfa.json"

print(bearer_token(service_account_file, credential_scopes))
