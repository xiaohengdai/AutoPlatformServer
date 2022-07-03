from flask import Flask
from flask import jsonify
from flask_cors import CORS


from celery import Celery

from app.api.api_asyn import api_asyn
from app.api.api_sync import api
from app.config import config
from app.logs import setup_log
from app.util.model import db

app = Flask(__name__)
app.config.from_object(config)
# CORS(app,  resources=r'/*')
CORS(app, supports_credentials=True)
# cors = CORS(app, supports_credentials=True, resources={r"/api/*": {"origins": "*"}})
app.register_blueprint(api_asyn)
app.register_blueprint(api)

app.config['CELERY_BROKER_URL'] = 'redis://127.0.0.1:6379/1'  ## 配置消息代理的路径，如果是在远程服务器上，则配置远程服务器中redis的URL
app.config['CELERY_RESULT_BACKEND'] = 'redis://127.0.0.1:6379/2'  # 要存储 Celery 任务的状态或运行结果时就必须要配置
# 初始化Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
# 将Flask中的配置直接传递给Celery
celery.conf.update(app.config)
setup_log("testing")  #使用日志

@app.before_request
def _db_connect():
    db.connect()

# This hook ensures that the connection is closed when we've finished
# processing the request.
@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        db.close()


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
