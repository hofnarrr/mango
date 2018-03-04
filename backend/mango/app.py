from os import environ
from flask import Flask

from mango import extensions, bprints
from mango.config.defaults import (Config, DevelopmentConfig, ProductionConfig,
                                   TestingConfig)

"""
 1. instantiate Flask() - mango.app.create_app()
 2. configure Flask() app - mango.app.create_app()
 3. initialize extensions - mango.extensions.init_extensions(Flask())
 4. register blueprints - mango.bprints.register_blueprints(Flask())
    4.1. instantiate/import blueprint - blueprint.__init__.py
    4.2. if blueprint exposes api, import it - blueprint.__init__.py
    4.3. declare register_blueprints(Flask()) - blueprint.__init__.py
 5. return Flask() object to caller
"""
def create_app():

    app = Flask(__name__)

    """
    configuration order of precedence:
        1. configuration from the file MANGO_SETTINGS envvar points to
        2. default configuration values from mango.config.defaults based on
           MANGO_MODE={prod,test,dev}
        3. default configuration values from mango.config.defaults.Config
    """
    _configure_app(app)
    extensions.init_extensions(app)
    bprints.register_blueprints(app)

    if app.config['DEBUG']:
        _list_routes(app)

    return app

def _configure_app(app):
    # mapping between MANGO_MODE envvar and class names in config.defaults
    config_map = {
            'prod': 'ProductionConfig',
            'test': 'TestingConfig',
            'dev':  'DevelopmentConfig'
    }

    # load base defaults
    app.config.from_object('mango.config.defaults.Config')
    print('Loaded default configuration')

    # try to load configuration based on MANGO_MODE envvar
    try:
        app.config.from_object('mango.config.defaults.'
                               + config_map[environ.get('MANGO_MODE')])
        print('MANGO_MODE is ' + environ.get('MANGO_MODE') + ', loaded '
              + config_map[environ.get('MANGO_MODE')])
    except KeyError:
        print('MANGO_MODE not set, skipping loading mode specific '
              + 'configuration')
        pass

    # try to load from the file MANGO_SETTINGS envvar points to
    try:
        app.config.from_envvar('MANGO_SETTINGS')
        print('loaded MANGO_SETTINGS file: ' + environ.get('MANGO_SETTINGS'))
    except RuntimeError as e:
        print('Couldn\'t configure app from envvar MANGO_SETTINGS, skipping')
        print(e)
        pass

# DEBUG!
# tweaked from http://flask.pocoo.org/snippets/117/
def _list_routes(app):
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        line = urllib.parse.unquote("{:30s} {:25s} {}".format(rule.endpoint, methods, rule))
        output.append(line)

    print('{:30s} {:25s} {}'.format('endpoint', 'methods', 'rule'))
    print('### Route debug ############################################===--')
    for line in sorted(output):
        print(line)
