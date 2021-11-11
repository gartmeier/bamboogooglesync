from .app import sync


def handler(event, context):
    print('before sync')
    sync()
    print('after sync')
