import click

from mango import app

@click.command()
@click.option('--host', '-h',
              default='127.0.0.1',
              help='the hostname to listen on. default: 127.0.0.1')
@click.option('--port', '-p',
              default=5000,
              help='webserver port. default: 5000')
@click.option('--debug/--no-debug',
              default=False,
              help='toggle app debug mode. default: False')
def cli(host='127.0.0.1', port=5000, debug=False):
    """
    Launches flask builtin server.

    """

    mango = app.create_app()
    return mango.run(host=host, port=port, debug=debug)
