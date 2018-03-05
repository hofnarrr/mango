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
@click.option('--mode', '-m',
              default=None,
              help='mango app mode. default: None')
def cli(host='127.0.0.1', port=5000, debug=False, mode=None):
    """
    Launches flask builtin server.

    """

    mango = app.create_app(mode=mode)
    return mango.run(host=host, port=port, debug=debug)
