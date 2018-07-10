from flask import Flask
from flask_restful import Resource, Api
from flask import jsonify
import json
import platform

app = Flask(__name__)
api = Api(app)

class Status(Resource):
    def get(self):
        data = {}
        data['hello'] = 'world'
        data['python_version'] = platform.python_version()
        return json.dumps(data)

api.add_resource(Status, '/status')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

