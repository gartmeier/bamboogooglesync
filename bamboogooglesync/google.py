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

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        google_credentials,
        scopes=["https://www.googleapis.com/auth/admin.directory.user"],
    )

    credentials = credentials.create_delegated(user_email)

    return build("admin", "directory_v1", credentials=credentials)
