from flask import request
from flask_restful import Resource

class HelloResource(Resource):
    def get(self, subject='world'):
        return {'Hello': subject}

    def post(self):
        data = request.get_json()
        return {'Hello': data.get('hello') or 'world'}
