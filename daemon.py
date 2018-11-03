from flask import Flask, jsonify
from socket import gethostname
from uuid import uuid4 as uuid


app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({
        'hostname': gethostname(),
        'uuid': uuid()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
