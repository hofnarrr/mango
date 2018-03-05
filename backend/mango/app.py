from os import environ
from flask import Flask

from mango import extensions, bprints
from mango.config.defaults import ( #pylint: disable=unused-import
    Config,
    DevelopmentConfig,
    ProductionConfig,
    TestingConfig,)

def create_app(mode=None):
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

    app = Flask(__name__)

    _configure_app(app, mode)
    extensions.init_extensions(app)
    bprints.register_blueprints(app)

    if app.config['DEBUG']:
        _list_routes(app)
        _print_config(app)

    return app

# TODO: refactor to separate module
def _configure_app(app, mode):
    """
    configuration order of precedence:
        1. configuration from the file MANGO_SETTINGS envvar points to
        2. default configuration values from mango.config.defaults based on
           envvar MANGO_MODE={prod,test,dev}
        3. default configuration values from mango.config.defaults based on
           "mode"-parameter passed to create_app()
        4. default configuration values from mango.config.defaults.Config
    """

    # mapping between MANGO_MODE envvar and class names in config.defaults
    config_map = {
        'prod': 'ProductionConfig',
        'test': 'TestingConfig',
        'dev':  'DevelopmentConfig'
    }

    # 4. load base defaults
    app.config.from_object('mango.config.defaults.Config')
    # DEBUG
    print('DEBUG: Loaded default configuration')

    # 3. load default configuration based on 'mode'-parameter, if set
    try:
        if mode is not None:
            app.config.from_object('mango.config.defaults.'
                                   + config_map[mode])
            # DEBUG
            print('DEBUG: \'mode\'-parameter set, loaded ' + config_map[mode])
        else:
            # DEBUG:
            print('DEBUG: \'mode\'-parameter not set')
    except KeyError as e:
        # DEBUG
        print('DEBUG: no such mode \'' + mode + '\'.')

    # 2. try to load configuration based on MANGO_MODE envvar
    try:
        app.config.from_object('mango.config.defaults.'
                               + config_map[environ.get('MANGO_MODE')])
        # DEBUG
        print('DEBUG: MANGO_MODE is '
              + environ.get('MANGO_MODE')
              + ', loaded '
              + config_map[environ.get('MANGO_MODE')])
    except KeyError:
        # DEBUG
        print('DEBUG: MANGO_MODE not set, not loading mode specific '
              + 'configuration')

    # 1. try to load from the file MANGO_SETTINGS envvar points to
    try:
        app.config.from_envvar('MANGO_SETTINGS')
        # DEBUG
        print('DEBUG: loaded MANGO_SETTINGS file: '
              + environ.get('MANGO_SETTINGS'))
    except RuntimeError as e:
        #print('Couldn\'t configure app from envvar MANGO_SETTINGS, skipping')
        # DEBUG
        print('DEBUG: ', e)

# TODO: refactor to separate modules under lib/
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
    print('### Routes ##################################################===--')
    for line in sorted(output):
        print(line)

def _print_config(app):
    print('App config:')
    for key in app.config:
        print('{} = {}'.format(key, app.config[key]))

