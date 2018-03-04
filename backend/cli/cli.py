import os

import click

CMD_DIR = os.path.join(os.path.dirname(__file__), 'commands')
CMD_PREFIX = 'cmd_'

class CLI(click.MultiCommand):
    def list_commands(self, ctx):
        commands = []

        for filename in os.listdir(CMD_DIR):
            if filename.endswith('.py') and filename.startswith(CMD_PREFIX):
                commands.append(filename[len(CMD_PREFIX):-3])

        return commands

    def get_command(self, ctx, name):
        ns = {}

        filename = os.path.join(CMD_DIR, CMD_PREFIX + name + '.py')

        with open(filename) as f:
            code = compile(f.read(), filename, 'exec')
            eval(code, ns, ns)

        return ns['cli']

@click.command(cls=CLI)
def cli():
    pass
