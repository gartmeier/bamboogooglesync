import click

from .app import sync, update


@click.group()
def cli(*args, **kwargs):
    pass

cli.add_command(sync)
cli.add_command(update)


if __name__ == "__main__":
    cli()
