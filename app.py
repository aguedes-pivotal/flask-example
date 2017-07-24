from flask import Flask, jsonify, json
from socket import gethostname
from os import getenv

app = Flask(__name__)


@app.route("/")
def hello():
    vcap_services = getenv('VCAP_SERVICES')
    return jsonify({'message': 'hello world', 'hostname': gethostname(), 'services-bind': json.loads(vcap_services)}), 200


port = getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=port, threaded=True)