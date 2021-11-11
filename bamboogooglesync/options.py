import click

from .types import Secret

bamboo_subdomain = click.option(
    "--bamboo-subdomain",
    envvar="BAMBOO_SUBDOMAIN",
    help='If you access BambooHR at https://mycompany.bamboohr.com, then the subdomain is "mycompany".',
    required=True,
)

bamboo_api_key = click.option(
    "--bamboo-api-key",
    envvar="BAMBOO_API_KEY",
    help="See: https://documentation.bamboohr.com/docs/getting-started.",
    required=True,
)

google_admin = click.option(
    "--google-admin",
    envvar="GOOGLE_ADMIN",
    help="Google Workspace admin user email. See: https://developers.google.com/admin-sdk/directory/v1/guides/delegation",
    required=True,
)

google_credentials = click.option(
    "--google-credentials",
    default="credentials.json",
    envvar="GOOGLE_CREDENTIALS",
    help="Path to Google Workspace credentials.json. See: https://developers.google.com/admin-sdk/directory/v1/guides/delegation",
    required=True,
    type=click.Path(dir_okay=False, exists=True),
)
