from flask import Blueprint
from flask_restful import Api

from mango.blueprints.hello.resources import HelloResource

api = Api(prefix='/hello')
blueprint = Blueprint('hello', __name__)

api.add_resource(HelloResource, '/<string:subject>', '/')

api.init_app(blueprint)
