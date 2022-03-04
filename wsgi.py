from flask import Flask
from flask import jsonify
from flask_cors import CORS
from api.vision_api import vision


app = Flask(__name__)
# CORS(app,  resources=r'/*')
CORS(app, supports_credentials=True)
# cors = CORS(app, supports_credentials=True, resources={r"/api/*": {"origins": "*"}})

app.register_blueprint(vision, url_prefix='/api')


@app.errorhandler(Exception)
def error(e):
    ret = dict()
    ret["code"] = 1
    ret["data"] = repr(e)
    return jsonify(ret)


if __name__ == '__main__':
    app.run(host="172.17.156.247", port=8080, ssl_context=(
        "./mz1.top.pem",
        "./mz1.top.key"))
