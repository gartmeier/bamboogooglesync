# Bamboo Google Sync
A command line interface to synchronize BambooHR employees with Google Workspace users. The command uses the [BambooHR API](https://documentation.bamboohr.com/docs) and [Google Directory API](https://developers.google.com/admin-sdk/directory/v1/guides)

![Sequence Diagram](https://user-images.githubusercontent.com/661673/141306641-cd34dfee-815e-4dd0-bcfe-5eb49345ed49.png)

# Update Google Workspace Users
Before using Bamboo Google Sync for the first time, run the update command first. The command updates all employees' external IDs and organization units. The external id is later used by the synchronization command to get an employees user.
```console
Usage: python -m bamboogooglesync update [OPTIONS]

Options:

  --bamboo-subdomain TEXT    If you access BambooHR at
                             https://mycompany.bamboohr.com, then the
                             subdomain is "mycompany".  [required]
  --bamboo-api-key TEXT      See:
                             https://documentation.bamboohr.com/docs/getting-
                             started.  [required]
  --google-admin TEXT        Google Workspace admin user email. See:
                             https://developers.google.com/admin-
                             sdk/directory/v1/guides/delegation  [required]
  --google-credentials FILE  Path to Google Workspace credentials.json. See:
                             https://developers.google.com/admin-
                             sdk/directory/v1/guides/delegation  [required]
  --help                     Show this message and exit.
```
# Synchronize Google Workspace Users
The command gets information changed in the last 24 hours from BambooHR and updates users in Google Workspace by external id.
```console
Usage: python -m bamboogooglesync sync [OPTIONS]

Options:
  --bamboo-subdomain TEXT    If you access BambooHR at
                             https://mycompany.bamboohr.com, then the
                             subdomain is "mycompany".  [required]
  --bamboo-api-key TEXT      See:
                             https://documentation.bamboohr.com/docs/getting-
                             started.  [required]
  --google-admin TEXT        Google Workspace admin user email. See:
                             https://developers.google.com/admin-
                             sdk/directory/v1/guides/delegation  [required]
  --google-credentials FILE  Path to Google Workspace credentials.json. See:
                             https://developers.google.com/admin-
                             sdk/directory/v1/guides/delegation  [required]
  --help                     Show this message and exit.
```
