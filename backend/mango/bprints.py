from mango.blueprints.hello import blueprint as bp_hello

from mango.blueprints.hello import api as api_hello

# TODO: refactor maybe? implement blueprint autoloader?

def register_blueprints(app):

    app.register_blueprint(bp_hello, url_prefix='/hello')

    return None
