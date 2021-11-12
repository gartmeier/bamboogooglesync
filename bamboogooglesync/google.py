import json
import os

from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


def create_directory_service(user_email, google_credentials):
    """Build and returns an Admin SDK Directory service object authorized with the service accounts
    that act on behalf of the given user.

    Args:
      user_email: The email of the user. Needs permissions to access the Admin APIs.
    Returns:
      Admin SDK directory service object.
    """
    scopes = ["https://www.googleapis.com/auth/admin.directory.user"]

    if os.environ.get("IS_LAMBDA", "false") == "true":
        fn = ServiceAccountCredentials.from_json_keyfile_dict
    else:
        fn = ServiceAccountCredentials.from_json_keyfile_name

    credentials = fn(google_credentials, scopes=scopes)
    credentials = credentials.create_delegated(user_email)

    return build("admin", "directory_v1", credentials=credentials)
