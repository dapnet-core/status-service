
from flask import Flask, jsonify
#from flask_restful import Resource, Api
import platform

app = Flask(__name__)

@app.route('/status')
def api_status():
    data = {}
    data['hello'] = 'world'
    data['python_version'] = platform.python_version()
    return jsonify(data)

@app.route('/status/<servicename>')
def api_status_details(servicename):
    return 'You are reading ' + servicename

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

